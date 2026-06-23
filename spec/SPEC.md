# Bharat Direct — Open Protocol Specification

Version 0.1 (Working Draft). An open standard for aggregator-free, bank-to-bank merchant payments with risk-aware authorization and programmable split settlement. This document is a discussion draft for the payments ecosystem; it is not a product and not final.

---

## 1. Purpose and design goals

Bharat Direct defines how a merchant accepts a payment directly through a bank (no payment aggregator in the money path), how the rail attaches a fraud risk signal at the moment of authorization, and how a single customer payment can settle to multiple payees. It is designed to sit on top of existing real-time rails (UPI-class), reusing their authentication, mandates and tokenization rather than replacing them.

- **No rent layer.** A merchant connects to a sponsor bank / PSP directly. No aggregator collects a percentage in between.
- **Risk-aware by default.** Every authorization can carry a risk score that drives on-screen interventions (the Aware Layer).
- **Programmable settlement.** One payment may split natively to many payees in a single netted cycle, removing the need for pooled escrow.
- **Reuse, don’t rebuild.** Authentication, mandates, tokenization and identity (CKYC) are referenced, not reinvented.
- **Spec first.** Conformance is defined by this document so any bank, merchant platform or app can interoperate.

## 2. Actors

- **Payer.** The customer paying, holding an account at a Payer Bank.
- **Payee(s).** One or more recipients (merchant, marketplace sellers, commission account).
- **Merchant / Platform.** Initiates the payment request; may be a single seller or a marketplace.
- **Sponsor Bank / PSP.** The consortium bank that gives the merchant rail access. Replaces the PA.
- **Switch.** Thin, neutral router and net-settlement engine. Never custodies funds.
- **FIC.** Fraud Intelligence Consortium — returns a risk score; never receives raw PII.
- **Aware Layer.** Client-side component in the payer app that renders interventions based on the score.

## 3. Architecture overview

```
Merchant/Platform                 Sponsor Bank / Switch              Payer App
      |                                    |                              |
      |  POST /payments (+split manifest)  |                              |
      |----------------------------------->|                              |
      |                                    |  collect / intent --------->  |
      |                                    |        POST /risk/score ----> FIC
      |                                    |  <---------- riskScore ------- |
      |                                    |  authorize  [Aware Layer UI]  |
      |                                    |  <---- payerAuth (PIN/bio) --- |
      |                                    |  debit -> net settle -> credit(N payees)
      |  <---------- webhook: SETTLED -----|                              |
```

## 4. Core resources and endpoints

All endpoints are HTTPS, JSON, and require mutual authentication and request signing (Section 9). Base path: /v1.

| Method & path | Purpose |
| --- | --- |
| POST /payments | Initiate a payment (single or split). Returns a payment with state INITIATED. |
| GET /payments/{id} | Fetch payment state and settlement legs. |
| POST /payments/{id}/refund | Reverse all or part of a settled payment. |
| POST /risk/score | FIC: return a risk band + reasons for a proposed authorization. |
| POST /mandates | Create a recurring mandate (AutoPay-class). |
| POST /webhooks/test | Verify a merchant/bank webhook endpoint. |

## 5. The payment request (with split manifest)

A marketplace expresses the split inline. The sum of split amounts MUST equal amount. If splits is omitted, the whole amount settles to a single default payee.

```
POST /v1/payments
{
  "merchantId": "amzn-in",
  "orderRef": "AMZ-7781",
  "amount": 1000,
  "currency": "INR",
  "payer": { "handle": "customer@psp" },           // or null for intent flow
  "capture": "AUTO",
  "splits": [
    { "payee": "sellerA@bank", "amount": 400, "purpose": "GOODS" },
    { "payee": "sellerB@bank", "amount": 450, "purpose": "GOODS" },
    { "payee": "amzn-comm@bank", "amount": 150, "purpose": "COMMISSION" }
  ],
  "callbackUrl": "https://merchant.example/bd/webhook",
  "idempotencyKey": "AMZ-7781-1"
}
```

Response:

```
201 Created
{
  "paymentId": "pay_01HF...",
  "state": "INITIATED",
  "authUrl": "upi://pay?...",        // intent deep link, when payer not pre-bound
  "expiresAt": "2026-06-23T10:05:00Z"
}
```

## 6. The risk score (FIC) and the Aware Layer

Before the payer authorizes, the Payer Bank calls the FIC. The FIC returns a band and machine-readable reasons; it does NOT return raw data about other customers. The Aware Layer maps the band to an intervention.

```
POST /v1/risk/score
{
  "payerRef": "hash:9af1...",        // pseudonymous
  "payeeRef": "sellerA@bank",
  "amount": 1000,
  "context": { "newPayee": true, "channel": "INTENT", "screenShareDetected": false }
}
--> 200
{
  "band": "HIGH",                    // LOW | ELEVATED | HIGH | BLOCK
  "score": 0.86,
  "reasons": ["PAYEE_RECENT_FRAUD_REPORTS", "NEW_PAYEE", "AMOUNT_ANOMALY"],
  "payeeReports24h": 9
}
```

Intervention mapping (a conforming Aware Layer MUST implement at least these):

| Band | Required client behaviour |
| --- | --- |
| LOW | Frictionless. No interruption. |
| ELEVATED | Named-threat notice + payee reputation shown; single confirm. |
| HIGH | Unskippable cooling countdown + trance-breaker question ("Is someone instructing you to pay right now?") + active-recall confirm. |
| BLOCK | Prevent authorization; route to helpline / cooling period; log to FIC. |

Intervention outcome is reported back so the FIC learns which interventions stopped which losses:

```
POST /v1/risk/outcome
{ "scoreId": "rsk_01...", "shown": "HIGH", "userAction": "ABORTED", "abortReason": "TRANCE_BREAKER" }
```

## 7. Settlement model

The Switch computes net positions across all banks for a cycle and settles directly to each payee account. There is no pooled escrow and no intermediary float. Each split becomes an independent settlement leg with its own state.

```
GET /v1/payments/pay_01HF...
{
  "paymentId": "pay_01HF...",
  "state": "SETTLED",
  "legs": [
    { "payee": "sellerA@bank", "amount": 400, "state": "SETTLED", "utr": "..." },
    { "payee": "sellerB@bank", "amount": 450, "state": "SETTLED", "utr": "..." },
    { "payee": "amzn-comm@bank", "amount": 150, "state": "SETTLED", "utr": "..." }
  ]
}
```

## 8. Refunds, reversals and disputes

- **Refund.** POST /payments/{id}/refund with optional per-leg amounts; issued as a reversal message on the rail, not a card-style chargeback.
- **Dispute.** Raised through the consortium rulebook and online dispute resolution (ODR); the protocol carries dispute state but arbitration is governed off-band.
- **Liability.** For APP fraud, the protocol records the receiving-bank reference so a shared-liability rulebook can apportion loss (see whitepaper, Section 5).

## 9. Security and privacy

- **Transport & auth.** Mutual TLS; every request signed (detached JWS). Replay-protected with idempotencyKey and timestamp.
- **Idempotency.** POST /payments and refunds MUST be idempotent on idempotencyKey.
- **PII minimization.** The FIC receives pseudonymous references (hashed), never raw identity. Identity resolution stays with CKYC and the Payer Bank.
- **Federated learning.** Member banks contribute model gradients/signals, not raw customer rows. Conformant FIC nodes MUST NOT export raw PII across members.
- **Auditability.** Every score, intervention shown, and outcome is logged for supervision.

## 10. Error model

```
4xx/5xx
{ "error": "SPLIT_SUM_MISMATCH", "message": "splits must equal amount", "traceId": "..." }
```

| Code | Meaning |
| --- | --- |
| SPLIT_SUM_MISMATCH | Sum of splits != amount. |
| PAYEE_BLOCKED | A payee is BLOCK-banded by the FIC. |
| IDEMPOTENCY_CONFLICT | Reused key with different body. |
| MANDATE_REQUIRED | Recurring debit without a valid mandate. |

## 11. Conformance profiles

An implementation declares one or more profiles so partners know what it supports:

- **Profile M (Merchant).** Can initiate single-payee payments and handle webhooks.
- **Profile S (Split).** Adds programmable split settlement.
- **Profile A (Aware).** Implements the risk call and the full intervention mapping in Section 6.
- **Profile F (FIC node).** Serves /risk/score and participates in federated learning without exporting PII.

## 12. Reference implementation (planned modules)

| Module | Role | OSS |
| --- | --- | --- |
| bharat-direct-merchant | Server SDK + e-commerce plugins (WooCommerce/Shopify/Magento) — Profile M/S | Yes |
| bharat-direct-aware | Drop-in Aware Layer UI + risk client — Profile A | Yes |
| bharat-direct-fic | Risk-score API + mule-graph schema + federated-learning reference — Profile F (mock/sandbox first) | Yes (reference) |
| bharat-direct-spec | This document + OpenAPI + JSON schemas + conformance tests | Yes |

## 13. Versioning and governance

Semantic versioning on the protocol. Breaking changes increment the major version and the /v{n} base path. The specification is intended to be stewarded by a neutral, not-for-profit consortium (NPCI-style governance) with open membership, so no single vendor controls it. Until then this is an open discussion draft released for comment.

---

See the accompanying white paper "Bharat Direct — Finishing what UPI started" for the economic and policy rationale, sourced figures, and the fraud-psychology basis for the Aware Layer.


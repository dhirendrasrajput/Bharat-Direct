# Fraud Risk Consortium (FRC) — Stage 0 reference

A runnable, auditable reference for the **least scary version** of a shared fraud utility:
banks catch each other's mule accounts **without sharing any customer data**.

> **The principle:** share fingerprints of the guilty, never records of the innocent —
> and even the fingerprints never cross the wire in the clear.

## Why a bank can say "yes, we'll try"

| The fear | Why it doesn't apply here |
|---|---|
| "My customers' data leaves my walls" | It never does. The node runs inside your perimeter; only **blinded integers** cross the boundary. |
| "Competitors will see my customers" | You only ever contribute markers of **confirmed mule accounts** — never good customers — and those are hashed. |
| "The shared store is a honeypot" | The coordinator holds **only blinded hashes of known-bad accounts**. Breach it and there is nothing to steal. |
| "Queries leak who my customers pay" | **Private Set Intersection**: the coordinator never learns which payee you checked. |

## Architecture (federated: bank nodes + thin coordinator)

```
   Bank A node            Thin Coordinator             Bank B node
 (inside A's walls)     (holds only H(y)^b )        (inside B's walls)
        |   report mule (salted hash) |                     |
        |---------------------------->| store blinded marker|
        |                             |                     |
        |                             |  H(x)^a  (PSI query) |
        |                             |<--------------------|
        |                             |  H(x)^ab + {H(y)^b}  |
        |                             |-------------------->| match locally -> flag
```

The coordinator is deliberately dumb: it blinds and stores. All sensitive logic
(the payee check) finishes **inside the asking bank**.

## The asymmetric privacy design (read this)

- **Contribution = salted hash.** Confirmed mule accounts are already reported to police
  (1930 / NCRP), so sharing a *salted hash* of a known criminal account is low-sensitivity.
- **Query = full PSI.** The payee a bank checks may be a perfectly good account — so the
  query direction gets the stronger guarantee: the coordinator learns **nothing** about it.

This matches how trust actually grows: start by sharing only what is already shareable.

## Run it (synthetic data, zero real data, zero risk)

```bash
python fic/demo.py
```

You'll see Bank A report mules, Bank B catch them via PSI, clean accounts pass, and a
printed proof that only a 2048-bit integer crossed the network.

## Files

| File | Role |
|---|---|
| `psi.py` | Diffie-Hellman PSI primitives (hash, blind) — small and auditable |
| `coordinator.py` | The thin shared layer: stores only blinded markers |
| `node.py` | A bank-hosted node: `report_mule()` and `check_payee()` |
| `demo.py` | Two banks + coordinator on synthetic data |
| `schema/fraud_marker.schema.json` | The data contract — note: **no PII fields exist** |
| `openapi.yaml` | The HTTP API this in-process demo represents |
| `PILOT.md` | How a bank pilots this in a day |

## Conformance

This implements **Profile F** of the Bharat Direct protocol (see [`../spec/SPEC.md`](../spec/SPEC.md)):
serve risk checks and participate without exporting PII.

## Production hardening (intentionally out of scope for Stage 0)

This reference is optimised for *auditability and a fast pilot*, not production. Before real use:
- replace hash-mod-p with a vetted PSI library and hash-to-curve (RFC 9380);
- make contribution oblivious so the coordinator never sees even a salted hash;
- add mutual TLS, signed requests, idempotency, and consortium-governed **salt rotation**;
- add federated scoring (Stage 2) and golden-hour freeze coordination (Stage 3);
- get RBI Sandbox / RBIH cover before any live data.

See the white paper, Part B–I, for the full FRC blueprint.

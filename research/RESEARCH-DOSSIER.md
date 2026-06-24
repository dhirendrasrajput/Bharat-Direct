# Fraud Risk Consortium — Research Dossier

*A landscape review and evidence base, compiled before any architecture is committed. Positioned to inform and feed RBI's Digital Payments Intelligence Platform (DPIP), not to compete with it.*

**Status:** working research draft · **Scope:** India context, international precedents, legal foundations, privacy-preserving tech, graph ML, real-time architecture, intervention efficacy, liability models.

---

## 0. The one-paragraph reframe

India does not lack fraud-intelligence components — it lacks their **fusion and last mile.** The Reserve Bank, the Department of Telecom, and the Home Ministry are each building powerful but **siloed** systems: RBI's **DPIP** and **MuleHunter.ai**, DoT's **Financial Fraud Risk Indicator**, and I4C's **1930/NCRP**. None of them yet delivers a unified risk signal to the *one place fraud is consummated* — the consumer's screen at the moment of authorisation. The defensible, non-duplicative role for an open Fraud Risk Consortium (FRC) is therefore the **interoperability layer + the Aware Layer (last mile)** that fuses these silos and is governed by the legal and privacy lessons the world has already learned the hard way.

---

## 1. The problem and its scale

- Bank fraud rose ~3x to **₹36,014 crore in FY25** ([RBI annual report, via BusinessToday](https://www.businesstoday.in/technology/news/story/rbi-to-launch-digital-payments-intelligence-platform-for-fraud-prevention-432489-2024-06-07)); digital-payment fraud cases were **56.5% of all reported banking frauds** ([VisionIAS](https://visionias.in/current-affairs/news-today/2025-06-24/economy/rbi-and-banks-to-develop-the-digital-payment-intelligence-platform-dpip)).
- The dominant, fastest-growing vector is **authorized push-payment (APP) / social-engineering fraud**, which manipulates the *person*, not the system — so faster rails do not help.
- Mule accounts are the laundering substrate: criminal funds hop across many banks, and **no single institution sees the whole network**.

---

## 2. India's existing fraud-intelligence stack (the silos to fuse)

| System | Owner | What it does | Status / scale |
|---|---|---|---|
| **DPIP** (Digital Payments Intelligence Platform) | RBI / RBIH + 5–10 banks; committee under **A.P. Hota** (ex-NPCI MD) | Real-time intelligence-sharing DPI; ingests mule accounts, telecom, geo; **alerts before a transaction is processed** | Prototype; no launch date ([Business Standard](https://www.business-standard.com/industry/banking/rbi-banks-to-launch-dpip-platform-to-combat-rising-digital-payment-frauds-125062200370_1.html)) |
| **MuleHunter.ai** | RBI / RBIH | AI/ML mule-account detection; "infrastructure-level solution that integrates data from all participating banks and PSOs"; studied **19 mule behaviour patterns** | ~20 banks adopted; **95% accuracy at Canara Bank** ([Banking Frontiers](https://bankingfrontiers.com/rbi-introduces-mulehunter-ai-ai-driven-solution-to-detect-mule-accounts-developed-by-rbih/), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/)) |
| **Financial Fraud Risk Indicator (FRI)** + Sanchar Saathi / Chakshu / ASTR | DoT | Risk-classifies mobile numbers from telecom + FI + LEA inputs; enables banks/NBFCs/UPI to act pre-transaction; Mobile Number Revocation List | **~₹2,300 cr losses prevented in 10 months**; 88 lakh fraudulent connections cut ([StudyIQ](https://www.studyiq.com/articles/financial-fraud-risk-indicator/), [Tribune](https://www.tribuneindia.com/news/cyber-fraud/financial-fraud-risk-indicator-helps-prevent-cyber-fraud-losses-worth-rs-660-crore-within-six-months-of-launch)) |
| **1930 / NCRP / Citizen Financial Cyber Frauds Reporting & Mgmt System** | MHA / I4C | Citizen fraud reporting + rapid bank coordination for freeze/recovery | **₹8,189 cr saved across 23.6 lakh complaints**; **85-bank** coordination module ([NCRP/I4C](https://i4c.mha.gov.in/ncrp.aspx)) |

**The gap is explicit:** these are owned by three different ministries/regulators (RBI, DoT, MHA), and none delivers a fused signal to the point of authorisation. *Fusion + last mile* is the open opportunity.

---

## 3. International precedents and the lessons they encode

| System | Country | Model | The lesson |
|---|---|---|---|
| **TMNL** | Netherlands | 5 banks pooled ~10bn transaction records | ☠️ **Shut down 2024** — no legal basis under GDPR; EU AMLR now restricts sharing to high-risk only. **Never pool broad data; legal basis must come first.** ([ZQUAS](https://zquas.ai/tmnl.html)) |
| **COSMIC** | Singapore (MAS) | Share customer info **only when objective "red-flag" thresholds** are met; purpose-built law (FSMA Amendment Act 2023) + confidentiality safeguards | ✅ **Threshold-triggered sharing + a bespoke legal instrument.** ([MAS](https://www.mas.gov.sg/regulation/anti-money-laundering/cosmic)) |
| **CIFAS** National Fraud Database | UK | Not-for-profit membership; **reciprocity (must contribute to consume)**; 8 published Principles aligned to GDPR | ✅ **Governance template** — neutral, reciprocal, principle-bound. ([CIFAS](https://www.cifas.org.uk/about-cifas/governance)) |
| **AFCX** "Intel Loop" | Australia | Non-profit formed by banks; near-real-time sharing of scam **phone numbers, URLs, accounts**; multi-sector — banks + telcos + digital platforms + govt anti-scam centre + Meta | ✅ **Multi-sector fusion** — exactly the cross-silo model India needs. ([AFCX](https://www.afcx.com.au/)) |
| **FinCEN §314(b)** | USA | **Safe-harbor law** giving FIs liability protection to share fraud info voluntarily; 2026 guidance broadened to fraud; covers txn data, IPs, geo, device IDs, alerts | ✅ **The legal unlock is a *safe harbour*.** ([FinCEN](https://www.fincen.gov/resources/section-314b)) |
| **Confirmation of Payee** | UK | Payee name-check at the moment of payment | ✅ **Last-mile works:** 17% APP-fraud reduction (2023), **31% at Lloyds**, 2bn checks, 99% coverage. ([UK Finance](https://www.ukfinance.org.uk/news-and-insight/blogs/has-confirmation-payee-been-successful-combating-app-fraud)) |
| **PSR mandatory reimbursement** | UK | 50/50 liability split sending/receiving PSP; £85k cap | ✅ **The liability engine works:** 86% of losses returned in first 3 months; applies to all PSPs. ([Freshfields](https://www.freshfields.com/en/our-thinking/briefings/2024/09/authorised-push-payment-fraud-a-new-mandatory-reimbursement-regime-for-uk-psps)) |

**Distilled:** the survivors share *narrow, threshold-triggered markers* under an *explicit legal basis*, governed by a *neutral not-for-profit*, fuse *multiple sectors*, intervene at the *last mile*, and align incentives via *shared liability*. The one death (TMNL) did the opposite — broad pooling without a legal basis.

---

## 4. The legal foundation (India)

- **DPDP Act 2023** permits processing without consent for some "legitimate uses" and exempts processing **"for the prevention, detection or investigation of offences"** ([Cyril Amarchand](https://corporate.cyrilamarchandblogs.com/2023/12/fig-paper-no-28-data-law-series-2-implications-of-digital-personal-data-protection-act-2023-on-indian-banks/), [IndusLaw FAQs](https://cms-induslaw.com/en/ind/publication/sector-specific-faqs-on-the-digital-personal-data-protection-act-2023-dpdp-act-and-digital-personal-data-protection-rules-rules-2025)).
- **But** counsel warn that fraud-prevention as "legitimate use" is **"narrow, fact-specific, and litigation-prone, particularly for broad third-party disclosure."** This is the DPDP echo of the TMNL lesson.
- **Implication:** the FRC must (a) rely on the offence-detection basis, (b) restrict to **threshold-triggered confirmed/high-risk markers** (COSMIC model), and ideally (c) obtain an **explicit regulatory mandate or safe-harbour** (the FinCEN §314(b) / Singapore FSMA / EU AMLR mechanism). DPIP being a *regulator-led DPI* is precisely what can provide that legal cover — another reason to align with it.

---

## 5. Privacy-preserving technology survey

- **Private Set Intersection (PSI):** lets parties find common entities without revealing the rest — the standard mechanism for cross-bank entity alignment ([Sherpa.ai](https://developers.sherpa.ai/tutorials/entity-matching/vfl-and-psi/)).
- **Vertical Federated Learning (VFL):** parties hold *different features of the same entity*; PSI aligns entities, then a joint model trains without sharing raw rows. Banks predicting customer risk collaboratively is the canonical use case; **WeBank's FATE** is the leading open-source cross-silo platform ([VFL survey](https://arxiv.org/pdf/2304.01829)).
- **Advanced privacy:** VFL **without revealing intersection membership** (Private Set Union + synthetic samples, e.g. FLORIST), and **Tree-MPSI** for efficient multi-party alignment ([arXiv 2106.05508](https://arxiv.org/abs/2106.05508)).
- **Documented hard problems:** data **heterogeneity** across institutions, **identity-linkage** infeasibility (banks can't freely share identity), and **interaction/scale costs** ([Fed-RD](https://arxiv.org/pdf/2408.01609), [Starlit](https://eprint.iacr.org/2024/090.pdf)). These must be designed for, not hand-waved.

---

## 6. Graph ML for mule / network detection

- Mules and fraud rings are **relational** — high-degree nodes and dense sub-graphs reveal aggregation points that transaction-level models miss.
- Active approaches: GCN/GAT, **heterogeneous** and **dynamic** graphs; named systems include **LaundroGraph** (self-supervised AML), **DELATOR** (temporal graphs), **LineMVGNN**, and **NENN** (node+edge) ([Financial-fraud GNN review](https://www.sciencedirect.com/science/article/abs/pii/S0957417423026581), [collaborative AML](https://arxiv.org/pdf/2502.19952)).
- **India already has the production instance:** MuleHunter.ai (19 patterns, 95% accuracy). The FRC should *consume/extend* MuleHunter-class outputs, not rebuild them.

---

## 7. Real-time serving architecture (the latency reality)

- Standard three-layer pattern: **Kafka ingest → stream processing with windowed features → low-latency feature store** (Feast/Tecton/Redis) that scoring reads from ([Redis](https://redis.io/blog/real-time-fraud-detection/), [Confluent](https://www.confluent.io/blog/real-time-streaming-prevents-fraud/)).
- **Latency budgets:** fraud scoring **10–50 ms** inside a **<100 ms** authorisation window; payment <200 ms.
- **Scale proof:** Redis-class feature stores score **~700,000 transactions/sec** — UPI-scale is achievable with commodity streaming infra. The FRC's inline risk call must live inside this budget or it becomes mere after-the-fact analytics.

---

## 8. Intervention efficacy — the Aware Layer evidence base

| Intervention | Measured effect | Source |
|---|---|---|
| Confirmation of Payee (payee name-check) | **17%** APP-fraud reduction (2023); **31%** at Lloyds | [UK Finance](https://www.ukfinance.org.uk/news-and-insight/blogs/has-confirmation-payee-been-successful-combating-app-fraud) |
| Enhanced pre-payment, risk-based + call-to-action warnings | **15–25%** drop in high-risk payment completions | [TrustSphere](https://www.trustsphere.ai/post/authorised-push-payment-fraud-reimbursement-regimes-and-the-new-liability-landscape) |
| Mandatory reimbursement (incentive backstop) | **86%** of losses returned in first 3 months | [Freshfields](https://www.freshfields.com/en/our-thinking/briefings/2024/09/authorised-push-payment-fraud-a-new-mandatory-reimbursement-regime-for-uk-psps) |

**Conclusion:** the last-mile interventions the Aware Layer proposes are **evidence-backed, not speculative** — and effects are largest when warnings are *dynamic and tailored*, which is exactly what consortium-grade precision enables (and what defeats habituation).

---

## 9. Economic / liability model

The UK PSR **50/50 sending–receiving reimbursement** is the proven incentive engine: once the *receiving (mule-hosting) bank* shares liability, contributing high-quality signal becomes self-interest rather than charity. £85k cap covers 99% of claims; vulnerable consumers exempt from the excess. This is the mechanism that turns a shared utility from a perpetually under-funded "industry good" into a self-sustaining one.

---

## 10. Synthesis — design principles (what the research mandates)

1. **Fuse, don't rebuild.** Interoperate with DPIP, MuleHunter, FRI, and 1930/NCRP; add the missing fusion + last-mile layer.
2. **Legal basis first.** Threshold-triggered, confirmed/high-risk markers only; pursue regulatory mandate / safe-harbour. Never pool broad transaction data (TMNL).
3. **Threshold-triggered sharing** (COSMIC), not blanket sharing.
4. **Neutral, reciprocal, not-for-profit governance** (CIFAS / NPCI).
5. **Multi-sector** by design — bank + telecom + LEA + platforms (AFCX).
6. **Privacy is architectural** — PSI for alignment, VFL for scoring, no raw-PII export; design explicitly for heterogeneity, entity-linkage, and scale.
7. **Last mile is the point** — deliver the signal to the authorisation screen; evidence says this is where loss is actually prevented.
8. **Shared-liability incentive** to make contribution self-interested.
9. **Sub-100 ms or it's analytics**, not prevention.

---

## 11. Strategic positioning: the open layer that feeds DPIP

Bharat Direct's FRC is **not a competing platform**. It is:
- an **open protocol** for how fraud signals are represented, shared (threshold-triggered, privacy-preserving), and scored;
- the **Aware Layer** — the open, last-mile intervention SDK that turns DPIP/MuleHunter/FRI signals into a precise warning at the moment of payment;
- an **interoperability reference** that lets the existing Indian silos (and banks/PSPs/telcos) plug together;
- governed by the legal/governance lessons above so it is *adoptable* (COSMIC/CIFAS/§314(b)) rather than *litigation-prone* (TMNL).

This is the "open reference that feeds DPIP" stance — complementary, contributable, and filling a real gap rather than reinventing national infrastructure.

---

## 12. Open questions / further research before architecture is finalised

- **DPIP's published data model and APIs** (not yet public) — the FRC's interop spec must match these once available.
- **DPDP Rules 2025** fine print on fraud-prevention legitimate use and cross-entity disclosure.
- **Full read** of Fed-RD, Starlit, and the collaborative-AML papers for concrete VFL+PSI protocols and their measured overheads.
- **MuleHunter.ai integration surface** — what outputs RBIH exposes to banks.
- **Latency at Indian scale** — validating the <100 ms budget against UPI peak TPS.
- **Liability/legal feasibility in India** of a PSR-style shared-reimbursement model.
- **Behavioural RCT design** for the Aware Layer interventions in the Indian context (language, digital-arrest typologies).

---

## References

RBI DPIP — [Business Standard](https://www.business-standard.com/industry/banking/rbi-banks-to-launch-dpip-platform-to-combat-rising-digital-payment-frauds-125062200370_1.html), [BusinessToday](https://www.businesstoday.in/technology/news/story/rbi-to-launch-digital-payments-intelligence-platform-for-fraud-prevention-432489-2024-06-07), [VisionIAS](https://visionias.in/current-affairs/news-today/2025-06-24/economy/rbi-and-banks-to-develop-the-digital-payment-intelligence-platform-dpip) · MuleHunter.ai — [Banking Frontiers](https://bankingfrontiers.com/rbi-introduces-mulehunter-ai-ai-driven-solution-to-detect-mule-accounts-developed-by-rbih/), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/), [RBIH](https://rbihub.in/projects/mulehunter) · DoT FRI / Sanchar Saathi — [StudyIQ](https://www.studyiq.com/articles/financial-fraud-risk-indicator/), [Tribune](https://www.tribuneindia.com/news/business/dot-sebi-sign-mou-to-curb-misuse-of-telecom-resources-in-financial-frauds/) · I4C 1930/NCRP — [i4c.mha.gov.in](https://i4c.mha.gov.in/ncrp.aspx) · TMNL — [ZQUAS](https://zquas.ai/tmnl.html), [HRIF.EU](https://hrif.eu/en/2024/07/hrifstopstmnl/) · COSMIC — [MAS](https://www.mas.gov.sg/regulation/anti-money-laundering/cosmic) · CIFAS — [cifas.org.uk](https://www.cifas.org.uk/about-cifas/governance) · AFCX — [afcx.com.au](https://www.afcx.com.au/) · FinCEN §314(b) — [fincen.gov](https://www.fincen.gov/resources/section-314b) · Confirmation of Payee — [UK Finance](https://www.ukfinance.org.uk/news-and-insight/blogs/has-confirmation-payee-been-successful-combating-app-fraud) · PSR reimbursement — [Freshfields](https://www.freshfields.com/en/our-thinking/briefings/2024/09/authorised-push-payment-fraud-a-new-mandatory-reimbursement-regime-for-uk-psps) · DPDP & banks — [Cyril Amarchand](https://corporate.cyrilamarchandblogs.com/2023/12/fig-paper-no-28-data-law-series-2-implications-of-digital-personal-data-protection-act-2023-on-indian-banks/) · PSI/VFL — [VFL survey](https://arxiv.org/pdf/2304.01829), [arXiv 2106.05508](https://arxiv.org/abs/2106.05508), [Fed-RD](https://arxiv.org/pdf/2408.01609), [Starlit](https://eprint.iacr.org/2024/090.pdf) · Graph ML — [GNN fraud review](https://www.sciencedirect.com/science/article/abs/pii/S0957417423026581), [collaborative AML](https://arxiv.org/pdf/2502.19952) · Real-time architecture — [Redis](https://redis.io/blog/real-time-fraud-detection/), [Confluent](https://www.confluent.io/blog/real-time-streaming-prevents-fraud/).

*Compiled June 2026 for the Bharat Direct project. A living document — corrections and additions welcome via the repository.*

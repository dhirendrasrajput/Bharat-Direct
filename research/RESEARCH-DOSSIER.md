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

**The India liability gap (a key policy finding).** RBI's [2017 customer-liability circular](https://www.rbi.org.in/commonman/English/Scripts/Notification.aspx?Id=2336) grants **zero liability** only for ***unauthorised*** transactions (reported within 3 days; burden of proof on the bank). But **APP/scam fraud is *authorised* by the victim** — so it falls *outside* the zero-liability framework, leaving scam victims largely unprotected. This is precisely the hole the UK's reimbursement regime filled. It is both the strongest *citizen-protection* argument for the FRC and the natural place for a PSR-style shared-liability incentive to be introduced in India.

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

## 12. Gap closure (round 2) — what the deeper research resolved

| Gap (from round 1) | Resolution |
|---|---|
| DPIP data model / phasing | **Resolved (as far as public).** DPIP **Phase 1 = a negative registry** fusing telecom + I4C data to flag bad entities; **Phase 2 = instant AI risk scores → enhanced verification / temporary debit freezes** ([The420](https://the420.in/rbi-ai-digital-payment-fraud-detection-dpip/), [NextIAS](https://www.nextias.com/ca/current-affairs/25-06-2025/dpip-rbi-banks)). **DPIP's phasing mirrors the FRC roadmap exactly** — the FRC's Stage-0 negative registry *is* DPIP Phase 1. Exact APIs remain unpublished (RBIH prototype). |
| DPDP Rules 2025 fine print | **Resolved.** Notified **3 Jan 2025**; banks are data fiduciaries, large banks/PAs likely **Significant Data Fiduciaries** (extra duties); fraud-prevention "legitimate use" is **narrow/litigation-prone for broad disclosure**; the **legal-obligation basis needs no consent** — so a regulatory mandate (which DPIP supplies) is the cleanest legal footing ([IndusLaw](https://cms-induslaw.com/en/ind/publication/sector-specific-faqs-on-the-digital-personal-data-protection-act-2023-dpdp-act-and-digital-personal-data-protection-rules-rules-2025), [PIB Rules](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190655)). |
| Crypto protocols (concrete) | **Resolved.** Beyond PSI+VFL (FATE/WeBank), lightweight **CSGM** (MinHash/LSH + Bloom filters + PSI for account alignment) detects cross-bank mule networks exchanging only **~13–75 MiB** of hashed representations, **O(n)** not O(n²), validated on a **200M-account Alipay dataset** ([arXiv 2502.19952](https://ar5iv.labs.arxiv.org/html/2502.19952)). Limits: two-party/single-day, no formal DP bounds yet — multi-party + DP is the open extension. |
| MuleHunter integration surface | **Resolved (intent).** RBIH explicitly frames it as **"an infrastructure-level facility which others can use,"** using databases from all banks/PSOs; banks/PSPs/apps are **"free to use their own fraud detection over and above MuleHunter"** — an open invitation to build the Aware Layer *on top* ([Business Standard](https://www.business-standard.com/finance/personal-finance/explained-rbi-has-a-new-ai-tool-mulehunter-ai-to-reduce-digital-frauds-124120900250_1.html)). Exact API surface still bank-private. |
| Latency at Indian scale | **Resolved.** UPI runs **~7,500 TPS average**, 21.6bn/month, 228bn in 2025 ([Elets](https://bfsi.eletsonline.com/upi-smashes-records-with-21-6-billion-transactions-in-december-2025/)). Redis-class feature stores score **~700,000 TPS** — the <100ms inline budget is feasible, especially scoping inline scoring to high-risk/new-payee subsets. |
| India liability feasibility | **Resolved (and significant).** Zero-liability covers only *unauthorised* transactions; **APP/scam fraud is *authorised* and uncovered** — the policy gap a PSR-style shared-reimbursement model would fill (see §9). |
| Behavioural RCT evidence | **Resolved (directional).** Point-of-payment interventions: CoP 17–31%, pre-payment warnings 15–25%. Educational RCTs (US ~2,000 adults; BIT Canada/OSC) show effects **persisting 3+ months** ([GFLEC](https://gflec.org/wp-content/uploads/2021/04/Burke-Kieffer-Mottola-Perez-Arce-Can-Educational-Interventions-Reduce-Susceptibility-to-Financial-Fraud-CB2021.pdf)). An India-context Aware-Layer RCT (language, digital-arrest typologies) is still to be designed/run. |

**Genuinely still open (carry as architecture assumptions):** DPIP's exact published APIs (await RBIH); a **multi-party, differentially-private** extension of the lightweight cross-bank graph-matching; and a **field RCT** of the Aware Layer in Indian languages/typologies.

---

## 13. Update — two lanes (DPIP vs DSN) and where the real gaps remain

A second national-scale effort has emerged that changes the map: the **Digital Suraksha Network (DSN)** — a **₹100 crore, private, volunteer-led** initiative by CoinDCX, launched early 2026 after impersonation scammers caused the wrongful arrest of its founders ([CoinDCX](https://coindcx.com/blog/coindcx-news/coindcx-announces-100-crore-fund-towards-digital-suraksha-network/), [Business Standard](https://www.business-standard.com/companies/news/coindcx-sets-up-rs-100-crore-fund-for-customer-education-after-arrest-126033001114_1.html)). It is fundamentally **different from DPIP** — a different lane, not a competitor.

### 13.1 The two lanes

| | **DPIP (and the state stack)** | **DSN** |
|---|---|---|
| Sponsor | RBI / RBIH + banks (state) | CoinDCX, volunteer-led (private) |
| Authority | Regulatory mandate | Voluntary |
| Scope | Bank-payment-rail fraud: mule accounts, risk scoring, freeze | Open fraud-intel API, pre-transaction link/platform verification, impersonation/fake domains, crypto |
| Acts | At the payment, bank back-end | **Upstream of the payment** — WhatsApp link-check helpline, LEA forensics, citizen education |
| Output | Risk scores/alerts to banks | Open API + citizen verification + a **standards working group** |

They are **complementary**: DPIP is the bank back-end; DSN is the open, consumer/platform-facing, *pre-transaction* layer. Notably, DSN already occupies several things one might have called "the gap after DPIP."

### 13.2 Coverage map — what is now owned vs. still thin

**Owned by a funded incumbent:** bank-rail detection / mule AI / scoring / freeze (DPIP, MuleHunter); last-mile payee name-check (NPCI VoP); telecom signal (DoT FRI); citizen reporting + freeze (I4C 1930); open fraud-intel API, pre-transaction link verification, impersonation/domains, crypto fraud, education, LEA forensics, a standards WG (DSN).

**Still thin / unowned (the genuine post-DPIP+DSN gaps):**
1. **A *neutral* interoperability standard** across all silos (DPIP + MuleHunter + FRI + 1930 + DSN + platforms). DSN runs a working group, but a single firm — a crypto exchange — cannot hold the *neutral* seat; that belongs to an iSPIRT/NPCI-type convenor.
2. **The authorised-fraud liability & reimbursement regime.** India's zero-liability rule covers only *unauthorised* transactions; APP/scam fraud the victim was tricked into authorising is uncovered. Neither DPIP nor DSN is a liability regime. This is the UK-PSR-shaped hole.
3. **India-specific last-mile intervention science** — beyond name-matching: trance-breaker prompts, typology-naming, dynamic friction, RCT-tested in Indian languages and scam typologies.
4. **Platform/messaging-side interception** of the persuasion phase (the AFCX-Meta model) — nascent.
5. **Cross-border** flows — weak across all efforts.

### 13.3 The contributor thesis (supersedes §11's "build" framing)

With **both lanes now funded** — state (DPIP) and open-private (DSN) — the window to *build and own* a broad fraud-intelligence platform is effectively closed for an independent party. The defensible, non-redundant value is to **contribute, influence, and standardise**:
- DSN **explicitly invites** banks, fintechs, lenders and stakeholders to participate, and funds a **multi-stakeholder standards working group** — a concrete, low-barrier door, and only months old.
- The three thinnest gaps (neutral interop standard, the APP-liability policy, India-specific intervention science) are precisely where an individual can add value as a **contributor/advocate**, widening the coverage of efforts like DSN rather than duplicating them.

**Conclusion:** the honest "worth trying" path is *contribution*, not ownership — bringing this research, the open-protocol thinking, and the Aware-Layer intervention design to DSN's working group and the policy debate.

---

## 14. Two axes of fraud detection — and the under-served one

A useful lens that cuts across every effort in this dossier: fraud detection happens on **two structurally different axes**, and most of the ecosystem sits on only one.

- **Axis 1 — Counterparty / identity reputation:** *"Is this entity, account, or artifact bad?"* Mule detection (DPIP, MuleHunter), domain/impersonation intel (DSN), telecom risk (FRI), and a growing set of **private artifact-reputation vendors** — both B2B *pre-decision* identity-risk APIs (correlating email/phone/device/IP/UPI/wallet/domain to flag synthetic, coordinated, or disposable actors) and B2C *consumer-checker* bots ("is this number/link/message a scam?"). This axis is **crowded**.
- **Axis 2 — Victim state / in-session manipulation:** *"Is a legitimate user, with a clean account and clean artifacts, being socially engineered into paying right now?"* This is the APP/scam case. The victim is reputable on every signal; the only tell is **behavioural and in-session** (tempo, hesitation, "acting under instruction," new high-risk payee under pressure). This axis is **under-served** — only NPCI's Verification of Payee partially touches it (a name-match), and RBI's proposed "frictions" gesture at it.

**The load-bearing insight:** *catching bad identities ≠ catching good people being manipulated.* Reputation systems — however full-spectrum across artifacts — structurally cannot see a clean-artifact victim talked into authorising a payment. The scarce, non-redundant capability is the **Axis-2 last-mile behavioural layer** (the Aware Layer): trance-breakers, dynamic friction, typology-naming at the moment of authorisation, tested in Indian languages and scam typologies. This is where a contributor adds value the crowded Axis-1 market does not.

## 15. Identity & credential handling — a zero-standing-identity upgrade

A privacy/architecture principle that strengthens *any* shared fraud layer (and is the precondition for banks/platforms to contribute data at all — see TMNL, §3, and DPDP, §4):

- **Biometrics are not secrets.** A face or fingerprint cannot be revoked once leaked, so it should only **unlock a local device or secure enclave** — never *be* the credential. The credential should be a **cryptographic proof, hardware-bound and session-bound** (the FIDO/passkey principle).
- **The hub never sees the human.** Spoke (edge) knows the person; the hub knows only **rotating virtual identities**; the identity→pseudonym mapping stays at the edge or inside a **regulated confidential-compute boundary**.
- **Per-session unlinkability.** Rotating identifiers prevent the hub from profiling across sessions — a stronger property than the *stable* salted hash used in the Stage-0 PSI reference (which is matchable across queries). This is a concrete upgrade to capture.
- **Audit stores proofs and decisions, not raw identity.** **Recovery requires multi-party approval**, not phone/OTP alone (which defeats SIM-swap/ATO).

**Why it matters:** this is what makes cross-institution correlation **DPDP-aligned and TMNL-proof**, and therefore what lets banks and platforms feed a shared layer without pooling raw identity. It turns a central vendor database into a *shareable fabric*.

**Honesty on novelty (what already exists in India):** UPI **VPAs** (virtual identifiers), **Aadhaar Virtual ID** + UID tokenization, RBI **card tokenization (CoFT)**, the **Account Aggregator** framework (consented, purpose-bound sharing), and **passkeys/FIDO** for the biometrics-aren't-secrets principle. The genuinely novel application is **per-session unlinkable rotating identifiers used for cross-bank fraud-signal correlation** — i.e., a fraud-intelligence hub that never accumulates a standing identity profile.

---

## References

RBI DPIP — [Business Standard](https://www.business-standard.com/industry/banking/rbi-banks-to-launch-dpip-platform-to-combat-rising-digital-payment-frauds-125062200370_1.html), [BusinessToday](https://www.businesstoday.in/technology/news/story/rbi-to-launch-digital-payments-intelligence-platform-for-fraud-prevention-432489-2024-06-07), [VisionIAS](https://visionias.in/current-affairs/news-today/2025-06-24/economy/rbi-and-banks-to-develop-the-digital-payment-intelligence-platform-dpip) · MuleHunter.ai — [Banking Frontiers](https://bankingfrontiers.com/rbi-introduces-mulehunter-ai-ai-driven-solution-to-detect-mule-accounts-developed-by-rbih/), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/), [RBIH](https://rbihub.in/projects/mulehunter) · DoT FRI / Sanchar Saathi — [StudyIQ](https://www.studyiq.com/articles/financial-fraud-risk-indicator/), [Tribune](https://www.tribuneindia.com/news/business/dot-sebi-sign-mou-to-curb-misuse-of-telecom-resources-in-financial-frauds/) · I4C 1930/NCRP — [i4c.mha.gov.in](https://i4c.mha.gov.in/ncrp.aspx) · TMNL — [ZQUAS](https://zquas.ai/tmnl.html), [HRIF.EU](https://hrif.eu/en/2024/07/hrifstopstmnl/) · COSMIC — [MAS](https://www.mas.gov.sg/regulation/anti-money-laundering/cosmic) · CIFAS — [cifas.org.uk](https://www.cifas.org.uk/about-cifas/governance) · AFCX — [afcx.com.au](https://www.afcx.com.au/) · FinCEN §314(b) — [fincen.gov](https://www.fincen.gov/resources/section-314b) · Confirmation of Payee — [UK Finance](https://www.ukfinance.org.uk/news-and-insight/blogs/has-confirmation-payee-been-successful-combating-app-fraud) · PSR reimbursement — [Freshfields](https://www.freshfields.com/en/our-thinking/briefings/2024/09/authorised-push-payment-fraud-a-new-mandatory-reimbursement-regime-for-uk-psps) · DPDP & banks — [Cyril Amarchand](https://corporate.cyrilamarchandblogs.com/2023/12/fig-paper-no-28-data-law-series-2-implications-of-digital-personal-data-protection-act-2023-on-indian-banks/) · PSI/VFL — [VFL survey](https://arxiv.org/pdf/2304.01829), [arXiv 2106.05508](https://arxiv.org/abs/2106.05508), [Fed-RD](https://arxiv.org/pdf/2408.01609), [Starlit](https://eprint.iacr.org/2024/090.pdf) · Graph ML — [GNN fraud review](https://www.sciencedirect.com/science/article/abs/pii/S0957417423026581), [collaborative AML](https://arxiv.org/pdf/2502.19952) · Real-time architecture — [Redis](https://redis.io/blog/real-time-fraud-detection/), [Confluent](https://www.confluent.io/blog/real-time-streaming-prevents-fraud/).

*Compiled June 2026 for the Bharat Direct project. A living document — corrections and additions welcome via the repository.*

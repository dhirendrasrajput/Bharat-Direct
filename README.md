# Bharat Direct

### Finishing what UPI started — an aggregator-free, bank-owned payments rail, and a shared Fraud Intelligence Consortium to close the human gap UPI left open.

![Status](https://img.shields.io/badge/status-working%20draft-orange)
![Spec License: CC BY 4.0](https://img.shields.io/badge/spec-CC%20BY%204.0-blue)
![Code License: Apache 2.0](https://img.shields.io/badge/code-Apache%202.0-green)
![Discussion](https://img.shields.io/badge/this%20is-a%20flag%2C%20not%20a%20product-lightgrey)

---

India built the hardest 80% of a modern payments system — **UPI, a bank-owned NPCI, and central CKYC.** Two inefficiencies remain. A private **payment-aggregator** layer still collects rent between merchants and banks, on rails the network no longer needs. And **authorized push-payment (APP) fraud** — where a person is *manipulated into authorising a real payment* — is the fastest-growing financial crime, and the one gap a faster rail does nothing to close.

**Bharat Direct is an open blueprint to fix both — and an open fraud-intelligence layer being built in the open, right now.**

> ⚑ **This is a flag, not a pitch for sale.** The blueprint is meant to become shared public infrastructure. The author can architect it and is building the fraud layer openly; owning national-scale infrastructure needs NPCI, the banks, RBI, or an anchor player. If that could be you — **the blueprint is yours to take.**

---

## The 30-second version

- **Pillar 1 — Direct Settlement Consortium.** Merchants connect directly to banks; funds settle bank-to-bank over a thin, neutral switch that never holds money; only identity (CKYC) stays central. International cards keep working through one co-owned, at-cost gateway, so merchants never hold card data and stay out of PCI scope.
- **Pillar 2 — Fraud Intelligence Consortium (FRC).** A shared, privacy-preserving (federated-learning) risk graph that powers an on-screen **Aware Layer** — precise warnings delivered at the *one moment that matters*: the instant of authorisation. Fraud is a network crime; only a shared view sees it whole.

Read the reasoning, the sourced numbers, and the psychology behind the Aware Layer in the **[white paper](docs/Bharat-Direct-Whitepaper.docx)**.

---

## Start here — pick your door

| If you are… | Read this | Why |
|---|---|---|
| **A policymaker / regulator (RBI, DFS, NPCI)** | [Concept Note](docs/Concept-Note.md) → [White paper](docs/Bharat-Direct-Whitepaper.docx) | The opportunity, the ask, and the sourced facts in two pages |
| **A bank / anchor player (Reliance, Tata, a consortium)** | [Concept Note](docs/Concept-Note.md) → [Deck](docs/Bharat-Direct-Deck.pptx) | The strategic, category-defining version |
| **A builder / engineer** | [SPEC.md](spec/SPEC.md) → [MANIFESTO.md](MANIFESTO.md) | The open protocol, conformance profiles, and how to integrate |
| **Press / public** | [Op-ed](docs/Op-Ed.md) → [Carousel (PDF)](docs/Bharat-Direct-Carousel.pdf) | The argument in plain language |
| **Just curious** | [MANIFESTO.md](MANIFESTO.md) | The whole idea in one short read |

---

## Repository contents

```
README.md            ← you are here
MANIFESTO.md         ← the idea in one read; the call to the ecosystem
spec/
  SPEC.md            ← the open protocol: pay-by-bank, risk hooks, split settlement, conformance
research/            ← evidence base BEFORE architecture
  RESEARCH-DOSSIER.md← landscape review: DPIP, MuleHunter, TMNL, COSMIC, CIFAS, AFCX, PETs, evidence
fic/                 ← Fraud Risk Consortium Stage-0 reference (PSI, federated) — illustrative
  demo.py            ← two banks catch each other's mules with zero data shared
  PILOT.md           ← how a bank pilots it in a day, with zero real data
docs/
  Bharat-Direct-Whitepaper.docx   ← full discussion paper + sourced data + precedents
  Concept-Note.md / .docx         ← 2-page forwardable note for decision-makers
  Op-Ed.md / .docx                ← ~600-word op-ed
  Bharat-Direct-Deck.pptx         ← pitch deck
  Bharat-Direct-Carousel.pdf      ← square LinkedIn carousel
scripts/             ← the Python generators for the documents above
```

---

## For builders — the integration promise

The protocol is designed so **contributors and consumers integrate without ripping out their core systems:** one API, declared conformance **profiles** (Merchant / Split / Aware / FRC-node), federated by design, easy in and easy out. Start against the mock FRC and the Aware Layer reference, prove the fraud-reduction number on your own rails, then plug into the shared graph. See **[SPEC.md](spec/SPEC.md)**.

## Roadmap

| Stage | What | Status |
|---|---|---|
| 0 | Shared mule-account reporting hub (PSI, federated) | ✅ **Runnable reference in [`fic/`](fic/)** |
| 1 | Reputation graph + risk API + Aware Layer | Spec drafted; reference WIP |
| 2 | Federated models (no raw-data sharing) | Designed |
| 3 | Golden-hour freeze + shared liability | Designed (needs ecosystem) |
| 4 | Direct settlement rail + native split | Blueprint (needs NPCI / anchor) |

---

## Get involved

- **Build / critique:** open an [issue](https://github.com/dhirendrasrajput/Bharat-Direct/issues) — cite the section, the actor, and the failure mode. See [CONTRIBUTING.md](CONTRIBUTING.md).
- **Partner:** banks, PSPs, fraud teams, researchers, and anchor owners are especially welcome — see *Contact* below.
- **Carry it forward:** if you're at iSPIRT, NPCI, a bank, or a player big enough to anchor this, the blueprint is yours to take.

## 📫 Contact / reach me

- **Email:** dhirendrasrajput@gmail.com
- **Issues & ideas:** https://github.com/dhirendrasrajput/Bharat-Direct/issues
- **Discussions:** enable GitHub *Discussions* on this repo for open conversation (Settings → Features → Discussions)
- **Author:** Dhirendra Rajput

If you can see merit and want to convene a conversation — even one I'm not in — please do, and tell me where I'm wrong.

---

## License & status

- **Specification & documents:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — share and adapt with attribution.
- **Reference code (scripts and future implementations):** [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).
- **Status:** working draft, released for examination and critique. Figures marked *secondary* in the white paper should be pinned to primary RBI/NPCI sources before formal circulation. This is a discussion starter, not financial, legal, or investment advice.

# Bharat Direct

*An open blueprint to finish what UPI started — and an open fraud-intelligence layer being built in the open, right now.*

---

## The problem

India built UPI, NPCI, and CKYC — the hardest 80%. Two things remain. A private aggregator layer still taxes payments on rails the network no longer needs. And authorized push-payment (APP) fraud — scams that manipulate the person, not the system — is the fastest-growing financial crime, untouched by any faster rail.

## The blueprint

- **Direct Settlement Consortium.** Bank-to-bank merchant payments, a thin neutral switch, no aggregator in the money path, cards handled by one at-cost gateway so no merchant holds card data.
- **Fraud Intelligence Consortium.** A shared, privacy-preserving risk graph + an on-screen Aware Layer that warns users at the moment of authorisation — rare, specific, and earned by real risk.

## What is open here

- **The protocol.** An open spec for direct pay-by-bank, risk-aware authorisation, and programmable split settlement. See SPEC.md.
- **The reference fraud layer.** A drop-in, federated, interoperable fraud-intelligence service + Aware Layer SDK.
- **The integration promise.** Contributors and consumers integrate without ripping out their core systems — one API, conformance profiles, federated by design, easy in and easy out.

## Who should build the rest

Owning national infrastructure is not a solo job. The rail and the full consortium need NPCI, the banks, RBI’s blessing, or an anchor with national scale. This repository is the blueprint and the fraud wedge — a flag for those who can carry it the rest of the way.

## How to join

1. Read SPEC.md and the white paper.
2. Build against the mock FRC and the Aware Layer SDK — prove the fraud win on your own rails.
3. Open an issue or reach out as a design partner: a bank, a PSP, a fraud team, or an anchor owner.

---

*This is meant to become shared public infrastructure. Contributions and critique are the point. Spec: CC BY 4.0. Code: Apache-2.0. Author: Dhirendra Rajput  ·  dhirendrasrajput@gmail.com  ·  June 2026.*


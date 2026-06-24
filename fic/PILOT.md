# Pilot the FRC in a day — with zero real data

A guide for a bank's fraud / risk / security team. The goal: let you evaluate the
shared mule-detection idea **without sharing a single byte of customer data**, and
decide for yourself whether it's worth a real pilot.

## What this is
A federated way for banks to catch each other's confirmed mule accounts. Each bank runs
a **node inside its own environment**. A thin **coordinator** holds only blinded hashes of
known-bad accounts. Queries use **Private Set Intersection** — the coordinator never learns
which payee you checked.

## Hour 1 — Read the code
It's deliberately tiny. Have your security team read `psi.py`, `coordinator.py`, `node.py`
(a few hundred lines total). Confirm for yourselves: **no customer record, account number,
name, or balance is ever sent.** Only blinded integers.

## Hour 2 — Run the synthetic demo
```bash
python fic/demo.py
```
Watch a mule reported by "Bank A" get caught by "Bank B" — and read the printed proof of
what actually crossed the network (one 2048-bit integer).

## Hour 3 — Run a node on YOUR confirmed-mule list (locally)
Point a node at your own list of **already-confirmed** mule accounts (the ones you've
reported to 1930 / NCRP). The node hashes them locally before anything leaves. Nothing about
your good customers is involved.

## Hour 4 — Connect to one peer
Stand up the coordinator (or connect to a sandbox one) and pair with **one** willing peer
bank. Each side reports its confirmed mules; each side queries a few test payees. Measure:
- how many of your in-flight suspicious payees light up from the peer's intelligence;
- how fast a freshly reported mule propagates.

## What leaves your bank (the whole list)
- At contribution: a **salted hash** of a confirmed mule account. Nothing else.
- At query: a **blinded integer** `H(payee)^a`. The coordinator cannot reverse it.
- What never leaves: customer names, account numbers, balances, transaction history,
  device data, or anything about good customers.

## What to show your risk committee
1. **Data-loss risk:** none by construction — read `psi.py`; the design is the guarantee.
2. **Legal posture:** you are sharing markers of accounts already reported as fraudulent —
   incremental to existing reporting, not novel data sharing.
3. **Value at N=1 and N=2:** useful for de-duplicating your own cases immediately; network
   effect begins with the first peer.
4. **Exit:** open source, no lock-in; stop any time, nothing of yours is held centrally.

## Then what
If it earns trust, the roadmap adds reputation scoring, federated models (still no raw data),
real-time inline checks feeding the Aware Layer, and golden-hour freeze coordination —
each stage earning the trust for the next. Start here, where there's nothing to fear.

**Questions / to pilot with a peer:** dhirendrasrajput@gmail.com

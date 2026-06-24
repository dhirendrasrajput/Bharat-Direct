# -*- coding: utf-8 -*-
"""
Bharat Direct — Fraud Risk Consortium (Stage 0) demo.

Shows two banks sharing CONFIRMED mule intelligence through a thin coordinator,
using Private Set Intersection so:
  * no raw account number ever leaves a bank,
  * the coordinator never learns which payee a bank checked,
  * a mule reported by Bank A is caught by Bank B in seconds.

Run:  python fic/demo.py     (or, from inside fic/:  python demo.py)
Uses only synthetic data. Zero real customer data. Zero data-loss risk.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    sys.stdout.reconfigure(encoding="utf-8")  # make emoji/output safe on Windows consoles
except Exception:
    pass

import psi
from coordinator import Coordinator
from node import BankNode


def hr(t=""):
    print("\n" + "=" * 64)
    if t:
        print(t)
        print("=" * 64)


def main():
    hr("BHARAT DIRECT — FRC Stage 0 (federated nodes + thin coordinator, PSI)")

    coord = Coordinator()
    bank_a = BankNode("Bank A", coord)
    bank_b = BankNode("Bank B", coord)

    # --- Bank A has confirmed some mule accounts from its own fraud cases ---
    confirmed_mules = ["ACC-MULE-1001", "ACC-MULE-2042", "vpa-scammer@okbank"]
    print("\nBank A reports CONFIRMED mules (only salted hashes leave Bank A):")
    for m in confirmed_mules:
        bank_a.report_mule(m)
        print(f"   reported  {m}")
    print(f"\nCoordinator now stores {coord.size()} BLINDED markers (no account numbers, no PII).")

    # --- Bank B checks payees at the moment of authorization ---
    hr("Bank B checks payees BEFORE letting a customer pay")
    test_payees = [
        ("ACC-MULE-2042", "a mule A reported — B has never seen it before"),
        ("vpa-scammer@okbank", "another of A's mules"),
        ("ACC-GOOD-7777", "a clean, normal payee"),
        ("vpa-honest-shop@okbank", "a clean merchant"),
    ]
    for payee, note in test_payees:
        flagged = bank_b.check_payee(payee)
        verdict = "FLAGGED  ✋  (block / Aware-Layer warning)" if flagged else "clean    ✓"
        print(f"   {payee:<26} -> {verdict}   [{note}]")

    # --- Show the privacy properties concretely ---
    hr("What actually crossed the network (privacy proof)")
    a = psi.new_secret()
    hx = psi.hash_to_int("ACC-MULE-2042", coord.salt)
    q = psi.blind(hx, a)
    print("When Bank B checked 'ACC-MULE-2042', the coordinator received only:")
    print(f"   Q = {str(q)[:60]}...  (a 2048-bit integer)")
    print("From Q the coordinator CANNOT recover 'ACC-MULE-2042' (discrete-log hard).")
    print("Bank B only learned a yes/no for ITS OWN query — never the list of accounts.")
    print("\nResult: cross-bank mule detection with NO raw data shared, in either direction.")
    hr()


if __name__ == "__main__":
    main()

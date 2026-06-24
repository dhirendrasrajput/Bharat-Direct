# -*- coding: utf-8 -*-
"""
A bank-hosted FRC Node (Stage 0).

The node runs INSIDE the bank's perimeter. The bank's confirmed-mule list and
its customers' payees never leave in the clear — only blinded group elements
(meaningless integers) cross the boundary.

Two operations:
  report_mule(account)  -> contribute a CONFIRMED mule marker (salted hash out)
  check_payee(account)  -> PSI query: is this payee a known mule anywhere?
                           the queried account is NEVER revealed to the coordinator
"""
import psi


class BankNode:
    def __init__(self, name, coordinator):
        self.name = name
        self._coord = coordinator
        self.salt = coordinator.salt        # shared salt, distributed by consortium governance

    def report_mule(self, account: str):
        """Contribute a confirmed mule account. Only its salted hash leaves the node."""
        h = psi.hash_to_int(account, self.salt)
        self._coord.contribute(h)

    def check_payee(self, account: str) -> bool:
        """PSI membership test. Returns True if 'account' is a known mule in the
        shared registry — without revealing 'account' to the coordinator."""
        a = psi.new_secret()                      # fresh per-query secret
        hx = psi.hash_to_int(account, self.salt)
        q = psi.blind(hx, a)                        # H(x)^a  -> sent out (coordinator can't recover x)
        qb, blinded_markers = self._coord.psi_query(q)   # gets H(x)^(ab) and { H(y)^b }
        doubly_blinded = {psi.blind(by, a) for by in blinded_markers}   # { H(y)^(ab) }
        return qb in doubly_blinded                 # match iff x == some y

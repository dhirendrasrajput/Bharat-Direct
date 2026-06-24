# -*- coding: utf-8 -*-
"""
The thin Coordinator for the Fraud Risk Consortium (Stage 0).

What it holds:  ONLY blinded markers  { H(y)^b }  of CONFIRMED mule accounts.
What it never holds:  customer records, account numbers, names, balances, or
                      anything about good customers.

Even if this coordinator were fully breached, there is nothing to steal: the
store contains blinded hashes of accounts already known to be criminal.
"""
import psi


class Coordinator:
    def __init__(self, salt="bharat-direct-fic-v0"):
        self._b = psi.new_secret()          # coordinator's private blinding secret (never shared)
        self._blinded_markers = set()        # { H(y)^b } — the entire shared state
        self.salt = salt                     # shared, governance-distributed salt

    # --- contribution path (low sensitivity: confirmed criminals, hashed) ---
    def contribute(self, salted_hash_int: int):
        """A member submits H(y) (salted hash of a CONFIRMED mule account).
        The coordinator blinds it with its secret and stores H(y)^b."""
        self._blinded_markers.add(psi.blind(salted_hash_int, self._b))

    # --- query path (high sensitivity: PSI protects the asked-about payee) ---
    def psi_query(self, q_blinded: int):
        """A member sends Q = H(x)^a. The coordinator returns:
             Qb = Q^b = H(x)^(ab)        (it cannot recover x: 'a' is unknown)
             the blinded marker set { H(y)^b }
        The member finishes the match locally. The coordinator learns nothing
        about which payee was checked."""
        qb = psi.blind(q_blinded, self._b)
        return qb, list(self._blinded_markers)

    def size(self) -> int:
        return len(self._blinded_markers)

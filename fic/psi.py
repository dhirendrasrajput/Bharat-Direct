# -*- coding: utf-8 -*-
"""
Private Set Intersection (PSI) primitives for the Bharat Direct Fraud Risk Consortium.

Design goal: a bank can ask "is this payee a known mule?" WITHOUT revealing the
payee to the shared coordinator, and the coordinator's registry of bad accounts is
never revealed in the clear to the asking bank.

Scheme: Diffie-Hellman PSI (commutative blinding).
  H(x)   = salted hash of an identifier mapped into the group
  blind  = modular exponentiation with a private secret
  Because (H(x)^a)^b == (H(x)^b)^a, two parties can test equality of x and y
  without either learning the other's raw value.

NOTE (production hardening — intentionally out of scope for this Stage-0 reference):
  - use a vetted PSI library and hash-to-curve (e.g. RFC 9380) instead of hash-mod-p
  - oblivious contribution so the coordinator never sees even a salted hash
  - mutual TLS + signed requests + salt rotation governed by the consortium
This module is deliberately small and auditable so a bank's security team can read it.
"""
import hashlib
import secrets
import random

# RFC 3526 MODP Group 14 (2048-bit) prime. Discrete-log hardness lives here.
_P_HEX = """
FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B
E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9
DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510
15728E5A 8AACAA68 FFFFFFFF FFFFFFFF
"""
P = int("".join(_P_HEX.split()), 16)


def _is_probable_prime(n, k=12):
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for sp in small:
        if n % sp == 0:
            return n == sp
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Fail loudly at import if the prime was mis-transcribed.
assert _is_probable_prime(P), "PSI modulus P is not prime — check _P_HEX transcription"


def hash_to_int(value: str, salt: str) -> int:
    """Salted SHA-256 of an identifier, reduced into the group. Never reversible to the raw id."""
    digest = hashlib.sha256((salt + "|" + str(value)).encode("utf-8")).hexdigest()
    return int(digest, 16) % P


def new_secret() -> int:
    """A fresh private exponent in [2, P-2]. Never shared."""
    return secrets.randbelow(P - 3) + 2


def blind(element_int: int, secret: int) -> int:
    """Raise a group element to a private secret: element^secret mod P."""
    return pow(element_int, secret, P)

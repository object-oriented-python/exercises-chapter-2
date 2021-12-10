from math_utils.primes import isprime

def test_isprime():
    v = [(1, False), (2, True), (3, False), (4, True)]
    for t in v:
        assert isprime(t[0]) == t[1]
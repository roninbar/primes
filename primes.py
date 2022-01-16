import sys
from itertools import chain, count, dropwhile, takewhile, islice

sys.setrecursionlimit(10 ** 6)


def sieve(s, depth=1):
    def no_need_to_filter(n):
        # print(f"{n} {'>=' if p * p <= n else '<'} {p} * {p}")
        return not p * p <= n

    def not_div(n):
        # print(f"{n} {'is' if n % p == 0 else 'is not'} divisible by {p}")
        # print(f"{n} % {p} {'==' if n % p == 0 else '!='} 0")
        return n % p != 0

    p = next(s)
    yield p
    yield from sieve(chain(takewhile(lambda n: n < p * p, s),
                           filter(lambda n: n % p != 0,
                                  dropwhile(lambda n: n < p * p, s))),
                     depth + 1)


primes = sieve(count(2))

per_row = 10
for i in range(0, 10000, per_row):
    print(f"{i + 1:>5}-{i + per_row:<5}:", end='')
    for p in islice(primes, per_row):
        print(f"{p:8}", end='')
        # print(f"=> {p} is prime.")
    print()

import sys
from itertools import chain, count, dropwhile, takewhile, islice


# sys.setrecursionlimit(10**4)


def sieve(s, depth=1):
    def no_need_to_filter(n):
        print(f"{n} {'>=' if p * p <= n else '<'} {p} * {p}")
        return not p * p <= n

    def not_div(n):
        # print(f"{n} {'is' if n % p == 0 else 'is not'} divisible by {p}")
        print(f"{n} % {p} {'==' if n % p == 0 else '!='} 0")
        return n % p != 0

    p = next(s)
    yield p
    yield from sieve(chain(takewhile(no_need_to_filter, s),
                           filter(not_div,
                                  dropwhile(no_need_to_filter, s))), depth + 1)


primes = sieve(count(2))

for i in range(0, 10000, 20):
    # print(f"{i + 1:>5}-{i + 20:<5}:", end='')
    for p in islice(primes, 20):
        # print(f"{p:8}", end='')
        print(f"=> {p} is prime.")
    # print()

import sys
import time
from math import sqrt


def is_prime(i):
    for j in range(3, int(sqrt(i)+1), 2):
        if i % j == 0:
            return 0
    return 1


def count_primes(n):
    """Count number of primes up to n-1 (naively)."""
    cnt = 1
    for i in range(3, n+1, 2):
        cnt = cnt + is_prime(i)
    return cnt


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python primes.py n")
        sys.exit(0)
    n = int(sys.argv[1])
    t0 = time.time()
    res = count_primes(n)
    dt = time.time() - t0
    print(f"count_primes({n}) = {res} (run time {dt} seconds)")

import sys
import time


def fib(n):
    """Print the Fibonacci series up to n."""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fib.py n")
        sys.exit(0)
    n = int(sys.argv[1])
    t0 = time.time()
    res = fib(n)
    dt = time.time() - t0
    print(f"fib({n}) = {res} (run time {dt} seconds)")

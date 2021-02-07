# pyc - Python compiler

pyc aims to make it easier to compile Python files using Cython.

To compile Python file to binary:

```bash
pyc myfile.py
```

To compile and run Python file:

```bash
python-pyc myfile.py arg1 arg2 ...
```

Or alternatively

```bash
python -m pyc myfile.py arg1 arg2 ...
```

## Examples

Let's consider rather classical example, counting Fibonacci numbers using
recursion. The standard Pythonic way to implement this is as follows:

```python
# fib.py

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
```

```bash
python fib.py 40
```

```text
fib(40) = 102334155 (run time 22.680758237838745 seconds)
```

The point of this package is that user should have *easy ways* to convert the code
above to binary, potentially getting better performance. Compiling is done using
`pyc`:

```bash
pyc fib.py
./a.out 40
```

```text
fib(40) = 102334155 (run time 13.891845464706421 seconds)
```

Already nice speedup! There's couple of alternative ways to run code. First is
using `-m pyc`, like:

```bash
python -m pyc fib.py 40
```

So it's quite standard way how script are run from command line, just add `-m
pyc`. Another way is to use `python-pyc`, i.e.

```bash
python-pyc fib.py 40
```

In background, all these commands utilize Cython to convert script to embedded
binary. That is, all the nice features provided by Cython can be used.

By converting Python script to binary we already get quite nice performance
benefits as the run time of the script reduced from 22.7 to 13.9 seconds.
However, we can do much better by using Cython typing system. For example, create
the following `fib.pxd` file in the same directory where `fib.py` is:

```cython
# fib.pxd

cpdef int fib(int n)
```

With this small additional definition:

```bash
python -m pyc fib.py 40
```

```text
fib(40) = 102334155 (run time 0.29824018478393555 seconds)
```

Are we fast? Let's compare against pure c solution:

```c
// fib.c

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int fib(int n) {
    if (n < 2)
        return n;
    return (fib(n - 1) + fib(n - 2));
}

int main(int argc, char **argv) {
    clock_t t0;
    int n = atoi(argv[1]);
    t0 = clock();
    int res = fib(n);
    double dt = ((double)(clock() - t0)) / CLOCKS_PER_SEC;
    printf("fib(%d) = %d (run time %0.2f seconds)\n", n, res, dt);
}
```

```bash
gcc -O3 fib.c
./a.out 40
```

```text
fib(40) = 102334155 (run time 0.29 seconds)
```

In this particular example, C and Python solutions are equally fast.

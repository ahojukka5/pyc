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

import cython

@cython.locals(j=cython.int)
cpdef int is_prime(int i)

@cython.locals(cnt=cython.int, i=cython.int)
cpdef int count_primes(int n)

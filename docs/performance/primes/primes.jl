function is_prime(i)
    for j=3:2:round(Int, sqrt(i+1))
        i % j == 0 && return 0
    end
    return 1
end


function count_primes(n)
    cnt = 1
    for i = 3:2:n
        cnt += is_prime(i)
    end
    return cnt
end

count_primes(10)
n = parse(Int, ARGS[1])
t0 = time()
v = count_primes(n)
dt = time() - t0
println("count_primes($n) = $v (run time $dt seconds)")

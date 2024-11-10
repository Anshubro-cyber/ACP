def sieve_of_eratosthenes(limit):

    prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
    
        if prime[p]:
           
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(10, limit + 1) if prime[p]]


limit = 99
two_digit_primes = sieve_of_eratosthenes(limit)

print("Two-digit prime numbers:", two_digit_primes)

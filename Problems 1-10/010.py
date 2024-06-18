# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def prime_sieve(limit):
    """
    Generates a list of prime numbers using the Sieve of Eratosthenes algorithm.
    """

    is_prime = [True] * limit  # Create a list to track primality
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit, p):
                is_prime[i] = False

    primes = []
    for p in range(limit):
        if is_prime[p]:
            primes.append(p)

    return primes


def sum_of_primes(limit):
    """
    Calculates the sum of all prime numbers below the given limit.
    """

    primes = prime_sieve(limit)  # Generate primes using the sieve
    return sum(primes)  # Sum the list of primes


# Call the function to find the sum of primes below 2 million
result = sum_of_primes(2_000_000)
print(result)  # Output: 142913828922

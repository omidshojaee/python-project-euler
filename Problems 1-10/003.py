# The prime factors of 13195 are 5, 7, 13 and 29.
# what is the largest prime factor of the number 600851475143?


def largest_prime_factor(n):
    """
    Finds the largest prime factor of the given number n.
    """

    # Start with the smallest prime factor (2)
    factor = 2

    # Keep dividing the number by the factor while it's divisible
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor  # Divide the number by the factor and update it
        else:
            factor += 1  # Move to the next factor

    return n


# Call the function to solve the problem for 600851475143
result = largest_prime_factor(600_851_475_143)
print(result)  # Output: 6857

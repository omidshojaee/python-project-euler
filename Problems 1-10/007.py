# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?


def is_prime(n):
    """ "
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def nth_prime(n):
    """
    Finds the nth prime number.
    """
    count = 0  # Count of prime numbers found
    num = 2  # Start checking from 2

    while count < n:
        if is_prime(num):  # Check if num is prime
            count += 1
        num += 1

    return num - 1  # Return the last prime number found


# Call the function to solve the problem for the 10001st prime number
result = nth_prime(10001)
print(result)  # Output: 104743

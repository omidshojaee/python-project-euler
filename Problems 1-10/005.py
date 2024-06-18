# 2520 is the smallets number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(a, b):
    """
    Finds the greatest common divisor of two numbers.
    """
    while b != 0:
        a, b = b, a % b  # Repeatedly swap and find the remainder until b is 0
    return a  # The final value of a is the GCD


def smallest_multiple(limit):
    """
    Finds the smallest positive number that is evenly divisable by all numbers from 1 to limit.
    """

    result = 1  # Initialize the result
    for num in range(1, limit + 1):
        result = (result * num) // gcd(result, num)  # Calculate LCM using GCD

    return result


# Call the function to solve the problem for numbers 1 to 20
result = smallest_multiple(20)
print(result)  # Output: 232792560

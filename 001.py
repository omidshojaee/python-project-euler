# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(limit):
    """
    Finds the sum of all multiples of 3 or 5 below the given limit.
    """

    # Initialize a variable to store the sum
    sum = 0

    # Iterate through all natural numbers below the limit
    for num in range(1, limit):
        # Check if the number is divisible by 3 or 5
        if (num % 3 == 0) or (num % 5 == 0):
            # Add the number to the sum
            sum += num

    return sum


# Find the sum of all multiples of 3 or 5 below 1000
result = sum_of_multiples(1000)
print(result)  # Output: 233168

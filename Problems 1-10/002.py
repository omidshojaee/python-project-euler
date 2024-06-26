# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of even-valued terms.


def sum_even_fibonacci(limit):
    """
    Finds the sum of even-valued terms in the Fibonacci sequence below the given limit.
    """

    # Initialize the first two Fibonacci terms
    a, b = 1, 2

    # Initialize a variable to store the sum of even-valued terms
    sum = 0

    # Itertate while the current Fibonacci term (b) is below the limit
    while b <= limit:
        # Check if the current term is even
        if b % 2 == 0:
            # Add the even term to the sum
            sum += b

        # Calculate the next Fibonacci terms
        a, b = b, a + b

    return sum


# Call the function to solve the problem for a limit of four million
result = sum_even_fibonacci(4_000_000)
print(result)  # Output: 4613732

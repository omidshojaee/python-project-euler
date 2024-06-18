# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The squares of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of suqares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    """
    Calculates the sum of the squares of the first n natural numbers.
    """

    return sum(x**2 for x in range(1, n + 1))


def square_of_sum(n):
    """
    Calculates the square of the sum of the first n natural numbers.
    """
    return sum(range(1, n + 1)) ** 2


def difference_of_squares(n):
    """
    Calculates the difference between the sum of squares and the square of the sum of the first n natural numbers.
    """
    return square_of_sum(n) - sum_of_squares(n)


# Call the function to solve the problem for the first 100 natural numbers
result = difference_of_squares(100)
print(result)  # Output: 25164150

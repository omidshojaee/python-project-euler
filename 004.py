# A palindromic number reads the same both ways. The largest palindrome made from the product of 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    """
    Checks if the given number n is a palindrome.
    """
    return str(n) == str(n)[::-1]


def largest_palindrome_product(digits):
    """
    Finds the largest palindrome made from the product of two n-digit numbers.
    """

    largest_palindrome = 0  # Initialize to track the largest palindrome found
    start = 10 ** (digits - 1)  # Smallest n-digit number
    end = 10**digits - 1  # Largest n-digit number

    # Iterate through all possible combinations of the n-digit numbers
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product  # Update if a larger palindrome is found

    return largest_palindrome


# Call the function to solve the problem for 3-digit numbers
result = largest_palindrome_product(3)
print(result)  # Output: 906609

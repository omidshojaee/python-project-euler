# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def special_pythagorean_triplet(target_sum):
    """
    Finds the Pythagorean triplet (a, b, c) where a + b + c = target_sum and a^2 + b^2 = c^2.
    """

    # Iterate through possible values of a and b within the constraints
    for a in range(1, target_sum // 3 + 1):  # a must be less than one-third of the sum
        for b in range(
            a + 1, target_sum // 2
        ):  # b must be greater than a and less than half the sum
            c = target_sum - a - b
            if a**2 + b**2 == c**2:  # Check if it's a Pythagorean triplet
                return a * b * c  # Return the product if found

    return None  # Return None if no triplet is found


# Call the function to solve the problem for a sum of 1000
result = special_pythagorean_triplet(1000)
print(result)  # Output: 31875000

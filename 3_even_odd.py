"""
Write two functions, isOdd() and isEven(), with a single numeric parameter named
number. The isOdd() function returns True if number is odd and False if number is even. The
isEven() function returns the True if number is even and False if number is odd. Both
functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered
an even number.
"""

def is_odd(number_one):
    if number_one % 2 == 1:
        return True
    elif number_one == float:
        return False
    else:
        return False


print(is_odd(11))


def is_even(number_two):
    if number_two % 2 == 0:
        return True
    elif number_two == float:
        return False
    else:
        return False


print(is_even(10))

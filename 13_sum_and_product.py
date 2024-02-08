# SUM&PRODUCT
"""
Write two functions named calculateSum() and calculateProduct(). They both have a
parameter named numbers, which will be a list of integer or floating-point values. The
calculateSum() function adds these numbers and returns the sum while the
calculateProduct() function multiplies these numbers and returns the product. If the list passed
to calculateSum() is empty, the function returns 0. If the list passed to calculateProduct()
is empty, the function returns 1. Since this function replicates Python’s sum() function, your solution
shouldn’t call.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements’
conditions are all True:
"""


def calculate_sum(sum_numbers):
    result = 0
    for number in sum_numbers:
        result += number
    return result


def calculate_product(product_numbers):
    result = 1
    for numbers in product_numbers:
        result *= numbers
    return result


assert calculate_sum([]) == 0
assert calculate_sum([5, 5, 20]) == 30
assert calculate_product([]) == 1
assert calculate_product([5, 5, 4]) == 100

print(calculate_sum([]))
print(calculate_sum([15, 16]))
print(calculate_product([]))
print(calculate_product([5, 5]))

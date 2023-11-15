"""
Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1
up to and including upTo, the function prints one of four things:
 Prints 'FizzBuzz' if the number is divisible by 3 and 5.
 Prints 'Fizz' if the number is only divisible by 3.
 Prints 'Buzz' if the number is only divisible by 5.
 Prints the number if the number is neither divisible by 3 nor 5.
"""

def fizzbuzz(number):
    for i in range(1, number):
        if number % 5 == 0 and number % 3 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        else:
            return number


print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(11))

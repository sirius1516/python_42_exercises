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

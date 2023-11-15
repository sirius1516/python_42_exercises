"""
Write a convertToFahrenheit() function with a degreesCelsius parameter. This
function returns the number of this temperature in degrees Fahrenheit. Then write a function named
convertToCelsius() with a degreesFahrenheit parameter and returns a number of this
temperature in degrees Celsius.
"""

def convert_celsius_to_fahrenheit(celsius):
    celsius = celsius * (9 / 5) + 32
    return celsius


print(convert_celsius_to_fahrenheit(10))

fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(50))
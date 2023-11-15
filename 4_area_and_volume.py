"""
You will write four functions for this exercise. The functions area() and perimeter() have
length and width parameters and the functions volume() and surfaceArea() have length,
width, and height parameters. These functions return the area, perimeter, volume, and surface
area, respectively.
"""

def area(lenght, width):
    return lenght * width


print(area(5, 5))


def perimeter(lenght_p, width_p):
    return (lenght_p + width_p) * 2


print(perimeter(5, 5))


def volume(lenght_v, width_v, height_v):
    return lenght_v * width_v * height_v


print(volume(5, 5, 4))


def surface_area(lenght_s, width_s, height_s):
    return (lenght_s * width_s * 2) + (lenght_s * height_s * 2) + (height_s * width_s * 2)


print(surface_area(5, 5, 4))


assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(9999, 0, 9999) == 199960002
assert surface_area(5, 8, 10) == 340

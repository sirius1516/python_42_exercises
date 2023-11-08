def ordinal_suffix(number):
    number = str(number)
    if number.endswith('1'):
        return number + 'st'
    elif number.endswith('2'):
        return number + 'nd'
    elif number.endswith('3'):
        return number + 'rd'
    elif number.endswith('11'):
        return number + 'th'
    else:
        return number + 'th'


print(ordinal_suffix(0))
print(ordinal_suffix(1))
print(ordinal_suffix(2))
print(ordinal_suffix(3))
print(ordinal_suffix(4))
print(ordinal_suffix(11))


assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'


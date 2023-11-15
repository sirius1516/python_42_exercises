"""
Write a program that, when run, greets the user by printing ―Hello, world!‖ on the screen. Then it
prints a message on the screen asking the user to enter their name. The program greets the user by
name by printing the ―Hello,‖ followed by the user’s name.
"""

def hello_user():
    print('Hello World!')
    name = input('Enter the name: ')
    return f'Hello, {name}'


print(hello_user())
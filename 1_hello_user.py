def hello_user():
    print('Hello World!')
    name = input('Enter the name: ')
    return f'Hello, {name}'


print(hello_user())
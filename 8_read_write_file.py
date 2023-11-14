# 1 write to file
def write_to_file(filename, text):
    with open(filename, 'w') as write_file:
        write_file.write(text)


write_to_file('8_write_to_function.txt', 'This function is writing text')

# 2 append to file function
def append_to_file(filename, text):
    with open(filename, 'a') as write_file:
        write_file.write(text)


append_to_file('8_write_to_function.txt', '\nThis is append text.')


# 3 read from file function
def read_from_file(filename):
    with open(filename, 'r') as write_file:
        content = write_file.read()
        print(content)


read_from_file('8_write_to_function.txt')


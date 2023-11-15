"""
You will write three functions for this exercise. First, write a writeToFile() function with
two parameters for the filename of the file and the text to write into the file. Second, write an
appendToFile() function, which is identical to writeToFile() except that the file opens in
append mode instead of write mode. Finally, write a readFromFile() function with one parameter
for the filename to open. This function returns the full text contents of the file as a string.
"""
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


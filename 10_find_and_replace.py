'''
Write a findAndReplace() function that has three parameters: text is the string with text to
be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
'MY DOG JONESY' won’t be replaced.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements’
conditions are all True:
'''


def find_and_replace_text(text, old_text, new_text):
    replaced_text = ''
    i = 0
    while i < len(text):
        if text[i:i + len(old_text)] == old_text:
            replaced_text += new_text
            i += len(old_text)
        else:
            replaced_text += text[i]
            i += 1
    return replaced_text

assert find_and_replace_text('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace_text('fox', 'fox', 'dog') == 'dog'
assert find_and_replace_text('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace_text('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace_text('The Fox and fox', 'fox', 'dog') == 'The Fox and dog'


text = 'I don\'t like sun'
old_text = 'sun'
new_text = 'wind'
replaced_text = find_and_replace_text(text, old_text, new_text)
print(replaced_text)
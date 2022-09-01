import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    if match := re.search(string, text):
        print(f'Found "{string}" in "{text}"')
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print(f'Did not find "{string}"')
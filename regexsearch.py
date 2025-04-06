import os
import re
import pprint
files = []
for file in os.listdir('.'):
    if file.endswith('.txt'):
        files.append(file)
user_expression = input('What expression are you looking for?\n')
search_regex = re.compile(user_expression, re.I)

file_list = []
for filename in files:
    open_file = open(filename)
    read_file = open_file.read()
    if search_regex.search(read_file):
        file_list.append(filename)

pprint.pprint(file_list)
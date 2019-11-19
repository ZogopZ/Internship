# Exercise 1

import re

prompt = "Please, enter your name, age and copies separated by comma or space\n\n"
user_input = input(prompt)

pattern = r'\w+'
input_list = re.findall(pattern, user_input)

name = input_list[0]
age = int(input_list[1])
copies = int(input_list[2])

print(user_input)
print(input_list)
print(name, age, copies)

# Exercise 1

import re
import datetime

prompt = "Please, enter your name, age and copies separated by comma or space\n"
user_input = input(prompt)  # Get user's input and store it as a string.

pattern = r'\w+'    # This is the pattern that will be used with findall() below to separate the user_input.
input_list = re.findall(pattern, user_input)    # Find all alphanumeric words inside user_input.

name = input_list[0]
age = int(input_list[1])
copies = int(input_list[2])

year = datetime.date.today().year   # Find current year.
years_until_100 = 100 - age     # Calculate how many years until the user reaches a hundred years old.
year_turning_100 = year + years_until_100   # Calculate the exact year that the user will be turning a hundred.

print("\n")
print(copies*("Hello " + name + ". " + "You will turn a hundred hears old in the year "
      + str(year_turning_100) + ".\n"))     # Print requested output.


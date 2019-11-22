# Exercise 5

import random

a_len = random.randrange(20)  # Generate a random integer to represent the length of list a.
b_len = random.randrange(20)  # Generate a random integer to represent the length of list b.


a = random.sample(range(1, 101), a_len)     # Generate a list of a_len length with random integers in range 1-100.
b = random.sample(range(1, 101), b_len)     # Generate a list of b_len length with random integers in range 1-100.

common_elements = []

for element_A in a:
    if element_A in common_elements:    # If an element is already inserted in the answer list, do not parse it.
        continue
    for element_B in b:
        if element_A == element_B:      # Found a common element not already in answer list.
            common_elements.append(element_A)   # Add it to the answer list.

print("Random generated list a: " + str(a))
print("Random generated list b: " + str(b))
print("\n---> Common elements: " + str(common_elements))

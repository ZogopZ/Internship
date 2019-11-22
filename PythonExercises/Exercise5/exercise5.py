# Exercise 5

import random

a_len = random.sample(range(10, 30), 1)[0]
b_len = random.sample(range(10, 30), 1)[0]

a = random.sample(range(1, 100), a_len)
b = random.sample(range(1, 100), b_len)

common_elements = []

for element_A in a:
    if element_A in common_elements:
        continue
    for element_B in b:
        if element_A == element_B:
            common_elements.append(element_A)

print("Random generated list a: " + str(a))
print("Random generated list b: " + str(b))
print("\n---> Common elements: " + str(common_elements))

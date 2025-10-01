# Programming Activity 1

# Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
# in the list.
# - Create the list and assign the values.
# - For loop through the values in the list.

colors = ["navy", "purple", "white"]

for i in colors:
    print("colors:", i)


# Programming Activity 2

for color in colors:
    for letter in colors:
        print("letter:", letter)
    print()


#Programming Activity 3

import random

rand_nums = []

for i in range(10):
    rand_nums.append(randon.randint(1,100))

print("random nums:", rand_nums)


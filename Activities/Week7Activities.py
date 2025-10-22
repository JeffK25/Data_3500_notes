# Programming Activity 1

# Write a program, and have the user enter their name and their favorite 
# color, as two separate variables. Write the sentence to a file using the 
# with command "<name>'s favorite color is <color>"
# - get two variables from user
# - use the with command to open the file
# - use the write function to write to the file

name = input("Enter your name: ")
color = input("Enter your favorite color: ")

with open("/workspaces/Data_3500_notes/Activities/sentence.txt", "w") as file:
    file.write((name), "'s favoirte color is " + (color))



# Programming Activity 2

# Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
# array from 0s to random numbers.

import numpy

np = numpy.zeros(100)
print(np)

np = numpy.random.randint(50,size =100)
print(np)
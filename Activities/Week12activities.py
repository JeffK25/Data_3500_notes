
# Programming Activity 1

# Write a program which asks the user for two numbers, stored in two variables num1 and num2. 
# Generate a multiplication table for all integers 1 through num1 and 1 through num2. 
# The bottom right entry in your table should have the product of num1 and num2. 
# The table must be stored in a 2D list. 
# The list must be created first with a nested for loop. 
# Then, the table should be printed by another nested for loop iterating through the 2D list.
# Steps:
# - store the variables.
# - create a list, and add empty lists to the list - however many your need from the variables above.
# - append the values to the lists.
# - use a nested for loop to iterate through the list and print the values.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

lst = []

for i in range(num1):
    lst.append([])

for i in range(1,num1+1):
    for j in range(1, num2+1):
        lst[i-1].append(i*j)

for i in range(num1):
    for j in range(num2):
        print(lst[i][j], end = " ")
    print()


# Programming Activity 2

# Write a program which asks the user their age and favorite color.  
# Store these values in a dictionary with keys "age" and "favorite_color".  
# Also save the 2D list from the previous activity in the dictionary with the 
# key "multiplication_table".
# print all the values in the dictionary by iterating through the keys 
# using a for loop.

age = input("What's your age? ")
color = input("What's your favorite color? ")

user = {}

user["age"] = age
user["favorite_color"] = color
user["multiplication_table"] = lst

for key in user:
    print(key, user[key])



# Programming Activity 3

# Write a program, which loads a json file "person.json" into a Python 
# dictionary. Change the contents of person["age"] by adding 1. Save the 
# updated dictionary to person.json, and verify the contents of person.json 
# have been updated.
# - load person.json in to a Python dictionary using the json.load() function
# - update the value of person["age"], increase by 1
# - save the Python dictionary to person.json
# - open person.json and verify the "age" value has increased by 1

import json

with open("person.json") as file:
    person = json.load(file)

print(person["age"])
person["age"] += 1
print(person["age"])

with open("person.json", "w") as file:
	json.dump(person, file, indent=4)



# Programming Activity 4

# Write a program that asks the user for two numbers. In a try statement, 
# attempt to divide number 1 by number 2.  If number 2 is a 0, print a 
# message in the except statement saying "Error, attempted to divide by zero"
# - create two variables, inputted by the user
# - in a  try: block attempt to divide num1 by num2
# - in a except: block print a message indicating divide by zero error
# - end program


num = input("Enter a number: ")
numtwo = input("Enter another number: ")

try:
     print(num/numtwo)
except:
     print("can't divide by zero")

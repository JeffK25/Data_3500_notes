# Programming Activity 1

# Write a program which can tell if a 3 digit number is a palindrome. 
#  - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
#  - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
#  - To get the 3rd digit alone, modulus by 10. 
#  - Check if the first digit and 3rd digit are the same. 
#  - If they are the same print("palindrome!!!!"). 
#  - Else print("not palindrome!")

x = int(input("Enter a 3 digit number: "))

dig1 = x//100
dig3 = x %10

if dig1 == dig3:
    print("palindrome!!!!")
else:
    print("not palindrome!")





# Programming Activity 2

# Write a program which can add up the numbers in the series:
# 1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
# create a variable for the denominator
# for loop for 1000 iterations
# start for loop at 1, go to 1000
# variable to track the sum
# What number is the result?

x = 2
Sum = 0

for i in range(1000):
    Sum = (1/x) + Sum
    x *= 2

print(Sum)




# Programming Activity 3

# Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
# - if a child is 12 years old or older, they can sit in the front, regardless of weight.
# - if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
# - if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
# - if a child doesn't meet the criteria above they cannot sit in the front seat.
# Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. 
# Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.

age = int(input("Enter child age: "))
weight = int(input("Enter child weight: "))

if age >=12:
    print("Child may sit in the front seat")
elif age == 11 and weight > 90:
    print("Child may sit in the front seat")
elif weight > 100:
    print("Child may sit in the front seat")
else:
    print("Child may not sit in the front")


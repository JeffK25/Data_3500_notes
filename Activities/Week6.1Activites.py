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


#Programming activity 4

rand_nums = []
for i in range(10):
    rand_nums.append(random.randint(1,100))

i = 0

for num in rand_nums:
    # rand_nums[counteri]
    # rand_nums[i+1]
    if rand_nums[i] %2 == 0 and rand_nums[i+1] %2 ==0:
        print(rand_nums[i])
        print(rand_nums[i+1])


#Programming activity 5
file = open("/workspaces/Data_3500_notes/AAPL.2023.txt")
print(file)

lines = file.readlines()
print(lines)

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

def avg_calculator(price):
    return sum(prices)/len(prices)

print(avg_calculator(prices))

#average for first 5 days

def avg_first5days(prices):
    sum(prices[0:5])/5

print(avg_first5days(prices[0:5]))



# Programming Activity 5.2 
# This activity is a continuation from the last one and is meant to help you with your homweork.
# Write a Python program to read in the stock prices from a file, into a list.
# Create a list of floats from the list of strings you read in, from step 2.
# Calculate the average of the first 4 days in your list.
# Calculate the average of the last 4 days in your list.
# In a for loop, calculate a 4 day moving average for the floats in the list.
# Add logic in the for loop to implement a simple moving average 
# trading strategy.
# Display the profit from the strategy, after the for loop has finished.

print()
def average_first4days(prices):
    sum(prices[0:4])/4

def average_last4days(prices):
    sum(prices[-1:-5])/4

print(average_first4days)
print(average_last4days)
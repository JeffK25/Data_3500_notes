#list slicing

states = ["North Carolina", "Wyoming", "Texas", "Massachusetts", "Pennsylvania", "Arizona", "Utah"]

#index of MA
print(states[3])

#slice operator

subset1 = states[1:4]
print(subset1)


#just the last element of our list
last_element = states[-1:]
print(last_element)

#reverse a list
reveresed_states = states[::-1]
print(reveresed_states)

#return everything except the last two elements
subset2 = states[:-2]
print(subset2)

#every other element
subset3 = states[::2]
print(subset3)

#sort
states.sort()
print(states)


#Programming activity 5
file = open("/workspaces/Data_3500_notes/AAPL.2023.txt")
print(file)

lines = file.readlines()
print(lines)

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

# def avg_calculator(price):
#     return sum(prices)/len(prices)

# print(avg_calculator(prices))

# #average for first 5 days

# def avg_first5days(prices):
#     sum(prices[0:5])/5

# print(avg_first5days(prices[0:5]))



#Programming activity 4

# rand_nums = []
# for i in range(10):
#     rand_nums.append(random.randint(1,100))

# i = 0

# for num in rand_nums:
#     # rand_nums[counteri]
#     # rand_nums[i+1]
#     if rand_nums[i] %2 == 0 and rand_nums[i+1] %2 ==0:
#         print(rand_nums[i])
#         print(rand_nums[i+1])
    

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

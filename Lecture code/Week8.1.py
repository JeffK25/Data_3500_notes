
# def find_the_target(num_list, k):
#     found = False
#     for i in num_list:
#         for j in num_list:
#             if i +j ==k:
#                 found = True
#                 break
#     return found

# given = [9, 3, 24, 16]
# k = 11

# print(find_the_target(given, k))



#list comprehension
#newlist = [expressison for item in iterable if condition == True]

mixed_data = [32, "hello", "world", 42.9, 12, 100, "Monday", 20]

nums = []
for item in mixed_data:
    if isinstance(item, int) == True:
        nums.append(item)

print(nums)


nums = [item for item in mixed_data if isinstance(item, int) == True]
print(nums)


#example 2
words = ["racecar", "banana", "level", "civic", "kayak", "pop", "poop", "Aggies", "spider"]
palindromes = [pal for pal in words if pal == pal[::-1]]

print(palindromes)


#example 3
text = "hello world"
letters = sorted([letter for letter in text if letter != " "])

print(letters)


#homework 4

# file = open("/workspaces/Data_3500_notes/AAPL.2023.txt")
# # print(file)

# lines = file.readlines()
# print(lines)

# prices = []
# for line in lines:
#     line = float(line)
#     prices.append(line)

# print (prices)


#list comprehension of HW 4

prices = [round(float(line),2) for line in open("/workspaces/Data_3500_notes/AAPL.2023.txt").readlines()]
print(prices)


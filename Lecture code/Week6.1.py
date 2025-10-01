# Ask for a list of integers and make it a variable
# Use a for loop to loop through the list and multiplies another variable equal to 1 by the next integer in the list
# We need a way to identify which iteration it is on so we can skip that number in the list so set another variable equal to 0 and...
# use an if statement to skip that iteration if it equals the variable

# input_list = [1,2,3,4,5]
# output_list = []

# for i in input_list:
#     product = 1
#     for j in input_list:
#         if i == j:
#             continue
#         product *= j 

#     output_list.append(product)

# print(output_list)


# colors = ['blue', 'green', 'red', 'pink']


# age = [20,21,22]
# age.append(19)
# print("ages:", age)
# age.pop(2)
# print("ages:", age)
# age.insert(2, 100)
# print(age)

#anagrams
word1 = input("enter the first word: ")
word2 = input("enter the second word: ")

word1_list = []
for letter in word1:
    word1_list.append(letter)

print("word1 lsit", word1_list)

word2_list = []
for letter in word1:
    word2_list.append(letter)

print("word2 lsit", word2_list)


word1_list.sort()
word2_list.sort()

if word1_list == word2_list:
    print("These words are anagrams")
else:
    print("These words are not anagrams")
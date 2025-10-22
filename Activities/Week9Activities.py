
#Programming activity 1
#write a python program that creates a list of all even numbers from 2 to 100 using list comprehension

lst = [num for num in range(2,101,2)]
print(lst)



# Programming Activity 2

# Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. 
# Use list comprehension to remove these spaces from each string in the list.

strings = []

for i in range(3):
    i = input("input a string: ")
    strings.append(i)
    
print(strings)

strings2 = [string.strip() for string in strings]

print(strings2)



# Programming Activity 3

# Write a Python program which asks the user their name.  
# Store their name in a string variable. Use the Upper() function to make 
# all of the letters in their name upper case. Then, print to the console: 
# welcome, NAME ALLCAPS!.
#  - using input get the user name
#  - change the string to be all upper case
#  - print to the console: "welcome, NAME ALLCAPS!" (adding an exclamation

name = input("Enter your name: ")
name = name.upper()
print("Welcome, ", name, "!")



# Programming Activity 4

# Create a variable that stores the sentence below, and print the sentence to 
# the console, before making any changes. Change the first letter in the 
# sentence to be capitalized. Change the first instance of Whoa to be whoa 
# (all lower case), and the second instance of Whoa to be WHOA(all upper case).  
# Append a exclamation point to the end of the sentence. 
# Then re-print the sentence to the console.

# sentence = "dude, I just biked down that mountain and at first I was like 
# Whoa, and then I was like Whoa"
#  - using the string variable sentence, change the first letter to upper 
#    case using capitalize()
#  - create a list called "words" that stores all the words in the sentence 
#    in a list using the split() function.
#  - change the first "Whoa" to "whoa", and the second "Whoa" to "WHOA".
#  - append an exclamation point.
#  - print the new sentence.

#set up sentence
sentence = "dude, I just biked down that mountain \
and at first I was like Whoa and then I was like Whoa"
print(sentence)
sentence = sentence.capitalize()

# split words on the spaces
words = sentence.split(" ")

first_whoa = True # set up a variable to track how many times we've seen whoa
i = 0
for word in words:
    if words[i] == "whoa" and first_whoa:
        words[i] = words[i].lower()
        first_whoa = False # set tracker to false
    elif words[i] == "whoa" and not first_whoa:
        words[i] = words[i].upper()
    else:
        pass
    i += 1

# output new sentence
new_sentence = ""
for word in words:
    new_sentence += " " + word

print(new_sentence)

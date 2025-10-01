
# #for loops
# for i in range(1,11):
#     print("i:", i)

# counter = 0
# for i in range(10):
#     counter += 2
#     print(counter)

# aggies = "Go Aggies" 
# for i in aggies:
#     print(i)

#while loops
# age = 9
# while age <= 20:
#     print("you are", age, "years old'")
#     age +=1

# import random
# secret_number = random.randint(1,100)
# guess = 101
# while guess!= secret_number:
#     guess = int(input("Guess the secret number: "))
#     if guess > secret_number:
#         print("Too high, guess again.")
#     elif guess < secret_number:
#         print("Too low, guess agian")
#     elif guess >100:
#         print("The number is less than 100")
#     else:
#         print("You got it")

#nested for loop
words = ["zamboni", "moist", "chocolate"]
for word in words:
    print("word:", word)
    for letter in word:
        print("letter:", letter)

#for lopp
counter = 0
sum = 0
for i in range(100):
    sum += (1/(2** counter))
    print("Sum:", sum, "iteration:", counter)
    counter +=1
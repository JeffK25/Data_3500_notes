#dynamic typing
# age = eval(input("How old are you? "))

# print("You are", age, "years old")


# # if statements
# evote = input("votes for Erin: ")
# ivote = input("votes for Isaac: ")

# if evote > ivote:
#     print("Erin wins")
# elif evote < ivote:
#     print("Isaac wins")
# elif evote == ivote:
#     print("It's a tie")


# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# num3 = input("Enter a number: ")

# print(min(num1, num2, num3))


#Aggie Basketball

student = input("Are you a USU student: (Yes or No) ")
HURD = input("Are you a member of HURD premium:(Yes or No) ")

if student == "Yes" and HURD == "Yes":
    print("You get in 15 min early")
elif student == "Yes":
    print("You get in for free")
else:
    print("You have to buy a ticket")
    faculty = input("Are you USU faculty: (Yes or No) ")
    if faculty == "Yes":
        print("You get a dicount")

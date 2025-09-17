
# Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
#  - Gen Beta 2025
#  - Gen Alpha 2013
#  - Zoomer 1997
#  - Millennial 1981
#  - Gen X 1965
#  - Baby Boomer 1946

# Get user input (year)
# if statement
# multiple elif statements
# print repective gen

year = int(input("What year were you born? "))

if year >= 2025:
    print("You are a Gen Beta")
elif year >= 2013:
    print("You are a Gen Alpha")
elif year >= 1997:
    print("You are a Zoomer")
elif year >= 1981:
    print("You are a Millennial")
elif year >= 1965:
    print("You are a Gen X")
elif year >= 1946:
    print("You are a Baby Boomer")



# Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
#  - continue the loop while age is greater than 1
#  - print each time "you were alive in year: " current_year
#  - decrease age and current_year by one each time
#  - add an else saying "you were born in year: " current_year

age = int(input("How old are you? "))
current_year = 2025

while age >= 1:
    print("You were alive in year: ", current_year)
    age-=1
    current_year -=1
print("You were born in year: ", current_year) 



# Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 

number = 5
for i in range(19):
    print(number)
    number +=5



# Write a program that prints all the multiples of 5, from 5 to 95 using a while loop

number = 5

while number<=95:
    print(number)
    number+=5

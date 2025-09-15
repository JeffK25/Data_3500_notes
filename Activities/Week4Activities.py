
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

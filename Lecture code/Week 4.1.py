#pseudo code

#Rock, Paper, Scissors
player1 = input("R, P, or S? ")
player2 = input("R, P, or S? ")

if player1 == player2:
    print("It's a tie")

elif player1 =="R":
    if player2 =="P":
        print("Player 2 wins")
    else:
        print("Player 1 wins")
elif player1 == "S":
    if player2 == "P":
        print("Player 2 wins")
    else:
        print("Player 1 wins")


#garbage collection

import gc

x = [1,2,3]
y = x
print("y:" y)



del x 

gc.collect()


#debugger

peanutallergy = True
lactoseintolerant = True

#see what foods we can have

if peanutallergy:
    print("You can't have this PB and J")
if lactoseintolerant:
    print("You can't have ice cream")
if peanutallergy and lactoseintolerant:
    print("You can't have peanut butter ice cream")




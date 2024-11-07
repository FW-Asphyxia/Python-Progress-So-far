import random

Choice = int(input("How Many Times do you Want to roll\n> "))
Player = int(input("Guess the total \n> "))

Rolls = 0
Counter = 0
while Rolls < Choice:
    Dice = random.randint(1, 6)
    print(Dice)
    Counter += Dice
    Rolls += 1
if Player == Counter:
    print("You win ")
else:
    print(f"You Lost The Total was", Counter)

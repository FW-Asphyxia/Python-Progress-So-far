import random
Heads = 0
Tails = 0
Flip_Count = 0
Flips = int(input("How Many Times Do You Want To Flip "))
while Flips > Flip_Count:
    Coin = random.randint(1, 2)
    Flip_Count += 1
    if Coin == 1:
        print("Heads")
        Heads += 1
    if Coin == 2:
        print("Tails")
        Tails += 1
if Heads > Tails:
    print("Head Came More Times Than Tails")
if Heads < Tails:
    print("Tails Came More Than Heads")
if Heads == Tails:
    print("Both Were Equal")
print("Stats Are: \n Heads:", Heads, "Tails:", Tails)

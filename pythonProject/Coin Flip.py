import random
User = int(input("How Many Times Do You Want to flip?\n> "))
heads = 0
tails = 0
flips = 0
while User > flips:
    coin = random.randint(1, 2)
    if coin == 1:
        print("Heads")
        heads += 1
        flips += 1
    if coin == 2:
        print("Tails")
        tails += 1
        flips += 1
if heads > tails:
    print(f"Stats Are:\n Heads {heads} Tails {tails}\nHeads Came more Than Tails")
elif heads < tails:
    print(f"Stats Are:\n Heads {heads} Tails {tails}\nTails Came more Than Heads")
else:
    print("Both are equal")
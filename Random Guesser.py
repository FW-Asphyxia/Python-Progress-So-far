import random
Secret_Number = random.randint(1, 10)
Guess_Count = 0
while Guess_Count < 5:
    Guess = int(input("Guess "))
    if Guess == Secret_Number:
        print("You win")
        break
    else:
        Guess_Count += 1
        if Guess_Count == 4:
            print("You Lost The Number Was", Secret_Number)
            break

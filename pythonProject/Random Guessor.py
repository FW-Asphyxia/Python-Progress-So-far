import random
try:
    number = random.randint(0, 10000)
    guess = int(input("Guess \n> "))
    while guess is not number:
        if guess < number:
            guess = int(input('Higher\n> '))
        elif guess > number:
            guess = int(input('Lower\n> '))
        else:
            print("You Won IG")
            break
except ValueError:
    print("Do Not add spaces and characters to your input")

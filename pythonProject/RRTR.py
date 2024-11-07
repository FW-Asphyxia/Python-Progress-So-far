import random
bullet_chamber = [0, 1, 2, 3, 4, 5]
current_round = 0
bullet = bullet_chamber[random.randint(0, 5)]
alive = True
single = -0
bot_bullet_chamber = 0
current_bot_round = 0
bot_choice = 0
bot_alive = True
state = input("Single Player or Vs Bot\n").lower()
if state == "single" or state == "single player":
    single = True
if state == "bot":
    single = False
while alive and single:
    player = (input("Spin or Shoot?\n> ")).lower()
    if player == "spin":
        current_round = bullet_chamber[random.randint(0, 5)]
        if current_round == bullet:
            alive = False
            print("...")
        else:
            print("You survived")
    if player == "shoot":
        current_round += 1
        if current_round == bullet:
            alive = False
            print("...")
        else:
            print("You survived")
while alive and not single:
    bot_bullet_chamber = [0, 1, 2, 3, 4, 5]
    current_bot_round = 0
    bullet_bot = bot_bullet_chamber[random.randint(0, 5)]
    bot_alive = True
    while bot_alive and alive and not single:
        bot = ['spin', 'shoot']
        bot_choice = bot[random.randint(0, 1)]
    player = (input("Spin or Shoot?\n> ")).lower()
    if player == "spin":
        current_round = bullet_chamber[random.randint(0, 5)]
        if current_round == bullet:
            alive = False
            print("...")
        if current_bot_round == bullet_bot:
            print("The bot", bot_choice, "It lost")
        else:
            print("You survived")
    if player == "shoot":
        current_round += 1
        if current_round == bullet:
            alive = False
            print("...")
        else:
            print("You survived")

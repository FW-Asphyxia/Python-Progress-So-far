import random

first = ["Violet", "Brave", "Socks", "Sad", "Violent", "Mr.", "Beast", "Bust", "Royal", "ToothBrush", "For", "Happy",
         "Bro", "Sis", "Code", "Weeb", "Gyatt", "Rizzler", "I", "Show", "Meat", "Its", "Not", "That", "Dumb", "Super",
         "Entity", "Sleepy", "Who's", "Imagine", "Having", "Trash", "Big", "Knight", "King", "Techno", "Blade",
         "Syndicate", "Shouted", "Try", "Rip", "Serenade", "Grenade", "Milk", "Just", "Kill", "The", "Hellish",
         "Phobia", "The", "Last", "Itz", "Red", "Blue", "Green", "Aqua", "Yellow", "White", "Black", "Dark", "Tired",
         "Weak", "What", "If", "I", "Did", "Not", "Run", "A", "Coward"]
second = ["Of", "For", "While", "In", "Why", "Them", "AKA", "Licking", "Mouth", "Stinking", "Brain", "Not",
          "Existing", "Ray", "Sincere", "Anti",
                                        "Father", "Buying", "Him", "Armed", "_", "Hah", "Lol", 'Vortex', "Gonna", "Lie",
          "One", "Day", "Or", "The",
          "Other", "Theres", "No", "Way", "He", "Doesnt", "Envixity", 'Hyper', "Hydro", "Pyro", "Necro", "Cryo", "Ohio",
          "Gyatt", "Us", "Among", "Great", "Kicked", "Teacher", "Tree", "Bad", "Master", "Skeleton", "Skull", "Of",
          "The", "Not", "Than", "Then", "Guy", "Light", "Fire"]
third = ["Demon", "Greater", "Stray", "Dogs", "Devil", 'Slayer', "Chainsaw", "Man", "Ghoul", "Lolipop", "GG",
         "Couple", "Phoenix", "Fat", "Fan", "Child", "One", "Piece", "Real", "Attack", "Titan", 'Tiger',
         "Bleached", "EZ", "Tire", "Destiny", 'Shipping', "Cargo", "WasTaken", "Home", "Alone", "So", "Sad",
         "Cause", "Like", "You", "Know", 'No', "Official", "Ships", "Up", "Author", "Now", "Exited", "Hero", "God",
         "Loves", "You", "Know", "Nothing", "It", "Me", "Guy", "YT", "TTv", "Bus", "Job", "Less", "Re", "Incarnated",
         "_"
         , "Fire", "Light"]
fourth = range(0, 30000)
users = int(input("Enter A Number "))
count = 0
rarity = []
panel = False
while not panel:
    Baller = str(fourth[random.randint(0, 2999)])
    A = first[random.randint(0, (len(first)) - 1)]
    B = second[random.randint(0, (len(second)) - 1)]
    C = third[random.randint(0, (len(third)) - 1)]
    D = fourth[random.randint(0, 2998)]
    user = A + B + C + str(D)
    print(user)
    count += 1
    if user not in rarity:
        rarity.append(user)
    else:
        print("DAMN BRO THAT'S RARE TO GET THE SAME NAME TWICE")
        break
    if count == users:
        panel = True

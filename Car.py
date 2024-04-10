Command = ""
Started = False
while True:
    Command = input("> ").lower()
    if Command == "start":
        if Started:
            print("car is Already started")
        else:
            Started = True
            print("Car started...")
    elif Command == "stop":
        if not Started:
            print("Already Stopped")
        else:
            Started = False
            print("Stopped.")
    elif Command != 'Quit':
        break
    elif Command == "help":
        print("Start- To Start \n Stop- To Stop \n Quit-  To Quit")
    else:
        print("No Command Found Named" "'", Command, "'", 'Type Help For Info...')

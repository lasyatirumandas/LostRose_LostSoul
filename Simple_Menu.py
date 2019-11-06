# Lasya Tirumandas
# CS30 P1
# October 29, 2019
# Simple Menu


Places = {'Enchanted Forest': {'Right', 'Left', 'Up', 'Down'},
        'Sherwood Forest' : {}, 'Conques France' : {}}
Beast_Room = {'Left' : {}, 'Right' : {'attack', 'defend'},
            'Forward' : {}}

print(f"Places:")
for place in Places.keys():
    print(f"{place}")

Location = input("Which realm do you want to go?")
if Location == 'Enchanted Forest':
    print("You are in the Enchanted Forest")
    print("You have found a sword on the ground and now it is yours.")
    forest = Places["Enchanted Forest"]
    for direction in forest:
        print(f"{direction}")
    Forest = input("Which direction do you want to travel in?")
    if Forest == 'Right':
        print("You moved to the right side.")
        print("There is a orge sleeping and we will let him sleep.")
    elif Forest == 'Left':
        print("You have moved to the left side and there is nothing here")
    elif Forest == 'Up':
        print("You have moved up and there is nothing here")
    elif Forest == 'Down':
        print("You have moved down and THERE IS A ROSE!!")
elif Location == 'Sherwood Forest':
    print("You are in the Sherwood Forest")
    print("Robin Hood greets you have made an alliance with him.")
elif Location == 'Conques France':
    print("You are in the Conques, Forest")

print(f"Beast Room's direction:")
for direction in Beast_Room.keys():
    print(f"{direction}")

Beast = input("Which direction do you want to travel in?")
if Beast == 'Left':
    print("You moved to the left side of the room. but there's nothing here.")
elif Beast == 'Right':
    print("You moved to the right side of the room.")
    print("You can hear the growls become louder & see a figure in the dark")
    print("The Beast wakes up with the sound of your footsteps and scent")
    Mode = Beast_Room["Right"]
    for modes in Mode:
        print(f"modes")
    Mode = input("What would you like to do?")
    if Mode == 'attack':
        print("You will attack the Beast")
        print("Robin says: Hey I will deal with him, you go put the rose")
    elif Mode == 'defend':
        print("You will defend yourself from him")
        print("One slash across your chest....")
        print("Game Ends")
elif Beast == 'Forward':
    print("You have moved forward in the room.")
    print("You found the case & you put the rose before Beast comes closer.")

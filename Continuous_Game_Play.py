# Lasya Tirumandas
# CS30 P1
# Nov 6, 2019
# Continuous Game Play


def play():
    # print the title
    print("Lost Rose, Lost Soul")
    # belle introduction
    print("Hi! I am Belle. The love of my life has been a Beast and will stay")
    print("as a Beast if you don't find the Rose, which will restore him into")
    print("a charming Prince, that he was once.")
    print("And You will help me restore my Beast.")
    # belle directions
    print("There are three places that you can visit and in one of these")
    print("places, you will find the Rose.")
    print("I have already informed Robin Hood about your arrival and he")
    print("will be waiting for you in Sherwood Forest.")
    print("Right now, you are in Conques, France.")
    print("Please come back here when you find the Rose.")
    # things to do
    Actions = ['Quit', 'Places']
    #directions
    Directions = ['Left', 'Right', 'Forward', 'Backward']
    # print list of valid actions
    print(Actions)
    while True:
        action_input = get_input("Action: ")
        if action_input in Actions:
            print(f"{action_input.title()}")
            if action_input == 'Quit':
                sys.exit()
            elif action_input


play()

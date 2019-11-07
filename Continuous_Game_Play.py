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
        action_input = get_command("Action: ")
        if action_input in Actions:
            print(f"{action_input.title()}")
            if action_input == 'Quit':
                break
            elif action_input == 'Places':
                choose_Enchanted_Forest()
                choose_Sherwood_Forest()
                choose_Conques_France()
        else:
            print("Invalid action")

# defining get command function for player input
def get_command(message):
    action_input = input(message)
    return action_input.lower()

# defining enchnated forest
def choose_Enchanted_Forest():
    print("You are in the Enchanted forest and you have found a sword on the")
    print("ground and now that is yours.")
    print(Directions)
    while True:
        direction_input = get_command('What direction?')
        if direction_input in Directions:
            print(f"{direction_input.title()}")
            elif direction_input == 'Left':
                print(f"Moving Left")
                print("Nothing is here")
            elif direction_input == 'Right':
                print(f"Moving Right")
                print("The orge is sleeping and you will let it sleep.")
            elif direction_input == 'Forward':
                print(f"Moving Forward")
                print("Nothing is here")
            elif direction_input == 'Backward':
                print(f"Moving Backward")
                print(f"You have found the Rose")
        else:
            print("Invalid Direction")

def choose_Sherwood_Forest():
    print("You are in the Sherwood forest and Robin Hood greets you.")
    print("Robin Hood and you have become alliances in this adventure.")
    print("Robin: I heard from Belle that you need assistance with something")
    print("and I will help you hold off the beast and I am willing to come") 
    print("with you")




play()

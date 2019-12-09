# Lasya Tirumandas
# CS30 P1
# Nov 6, 2019
# Continuous Game Play

# importing a file for exiting the game
import sys
# importing map file to print land map here
from Map import Map
# importing character file to print character here
from Character import Character
# things to do
Actions = {'Quit', 'Places'}
# directions
Directions = ['Left', 'Right', 'Forward', 'Backward', 'Quit', 'Places']
# Places
Locations = ['Enchanted Forest', 'Sherwood Forest', 'Conques France']


def play():
    """Function for the Introduction of the game"""
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
    # printing the map here
    Maps = Map("Maps")
    print(Maps.printing_map())
    # printing the characters here
    character = characters("Character Names")
    print(character.printing_characters())
    # print list of valid actions and the places inside option places
    for action in Actions:
        print(f"- {action}")
    while True:
        action_input = get_command("Action: ")
        for action_input in Actions:
            if action_input == 'Quit':
                sys.exit()
            # option for place input to go to another place
            elif action_input == 'Places':
                for location in Locations:
                    print(location)
                locations_inputs()
        else:
            print("Invalid action")


# defining get command function for player input
def get_command(message):
    """making the input captial"""
    action_input = input(message)
    return action_input.title()


def choose_Enchanted_Forest():
    """Function for what happens and your chooses in Enchanted Forest"""
    print("You are in the Enchanted forest and you have found a sword on the")
    print("ground and now that is yours.")
    # Options for direction input and what happens in each direction
    print(Directions)
    while True:
        direction_input = get_command('What direction?')
        if direction_input in Directions:
            print(f"{direction_input.title()}")
            if direction_input == 'Left':
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
            elif direction_input == 'Quit':
                sys.exit()
            elif direction_input == 'Places':
                for location in Locations:
                    print(location)
                # option for place input to go to another place
                locations_inputs()
        else:
            print("Invalid Direction")


def choose_Sherwood_Forest():
    """Function for what happens and your chooses in Sherwood Forest"""
    print("You are in the Sherwood forest and Robin Hood greets you.")
    print("Robin Hood and you have become alliances in this adventure.")
    print("ROBIN: I heard from Belle that you need assistance with something")
    print("and I will help you hold off the beast and I am willing to come")
    print("with you")
    print("You hear villagers whispering about the red rose.")
    print("And listening to their conversation, you realize that it is the")
    print("Rose you are looking for")
    print("VILLAGERS: I heard that the red rose to heal the beast is in the")
    print("Enchanted forest.")
    print("ROBIN: Let's go to the Enchanted Forest")
    # Options for action input
    for action in Actions:
        print(f"- {action}")
    while True:
        action_input = get_command("Action: ")
        for action_input in Actions:
            if action_input == 'Quit':
                sys.exit()
            # option for place input to go to another place
            elif action_input == 'Places':
                for location in Locations:
                    print(location)
                locations_inputs()
        else:
            print("Invalid action")


def choose_Conques_France():
    """Function for what happens and your chooses in conques france"""
    print("You are in France.")
    print("BELLE: Did you find the rose?")
    print("ROBIN: Yes yes we did!")
    print("BELLE: That's amazing!")
    print("ROBIN: We should hurry to the beast now and i will come with u.")
    print("BELLE: Boys get your weapons ready.")
    print("BELLE: There he is")
    print("This is the Beast room.")
    # Options for direction input and what happens in each direction
    print(Directions)
    while True:
        direction_input = get_command('What direction?')
        if direction_input in Directions:
            print(f"{direction_input.title()}")
            # Left options leads to nothing
            if direction_input == 'Left':
                print(f"Moving Left")
                print("Nothing is here")
            # this shows what happens when right option
            elif direction_input == 'Right':
                print(f"Moving Right")
                print("You can hear the growls louder and make out a")
                print("figure from the dark.")
                print("The beast awakes with the sound of your footsteps.")
                print("ROBIN: Hey I will deal with him, you go put the Rose.")
            # this shows what happens when forward option
            elif direction_input == 'Forward':
                print(f"Moving Forward")
                print("You found the case to put the rose before the beast")
                print("comes closer. The beast restores into human form, now.")
                print("You did it!!! Success")
            elif direction_input == 'Quit':
                sys.exit()
            # option for place input to go to another place
            elif direction_input == 'Places':
                for location in Locations:
                    print(location)
                locations_inputs()
        else:
            print("Invalid Direction")


def locations_inputs():
    """This function allows people to input which location they want to go"""
    location_input = get_command("Location: ")
    for location_input in Locations:
        if location_input == 'Enchanted Forest':
            choose_Enchanted_Forest()
        elif location_input == 'Sherwood Forest':
            choose_Sherwood_Forest()
        elif location_input == 'Conques France':
            choose_Conques_France()
        else:
            print("Invalid action")


# Calling the function play to play the game
play()

# Lasya Tirumandas
# CS30 P1
# Nov 6, 2019
# Continuous Game Play

# importing classes of MapTile
from Classes import MapTiles
# importing a file for exiting the game
import sys
# importing map file to print land map here
from Map import Map
# importing map file to print Corona
from Map import Map1
# importing character file to print character here
from Character import Character
# Games to pick
Games = ['BEAUTY AND THE BEAST', 'TANGLED']
# things to do
Actions = {'Quit', 'Places'}
# list of places to move to
Keyword = ['EF', 'ER', 'SF', 'SR', 'EL', 'EB', 'SL', 'SB']
Beast = ['BF', 'BR', 'BL']
Speacial = ['CB']


# Beast Story
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
    Maps.printing_map()
    # printing the characters here
    characters = Character("Character Names")
    characters.printing_characters()
    # print list of valid actions and the places inside option places
    for action in Actions:
        print(f"- {action}")
    while True:
        action_input = get_command("Action: ")
        if action_input == 'Quit':
            sys.exit()
        # option for place input to go to another place
        elif action_input == 'Places':
            tiles_moving()


def tiles_moving():
    """The function to show how to move from one place to another"""
    print("Pick a number to go to that place")
    for Keywords in Keyword:
        print(f"{Keyword.index(Keywords) + 1}. {Keywords}")
    while True:
        # input for the keyword list
        Keyword_input = get_command("Keyword: ")
        try:
            if Keyword_input == '1':
                MapTile = MapTiles('Forward')
                MapTile.Enchanted_forward()
            elif Keyword_input == '2':
                MapTile = MapTiles('Right')
                MapTile.Enchanted_right()
            elif Keyword_input == '3':
                MapTile = MapTiles('Forward')
                MapTile.Sherwood_forward()
            elif Keyword_input == '4':
                MapTile = MapTiles('Right')
                MapTile.Sherwood_right()
            elif Keyword_input == '5':
                MapTile = MapTiles('Left')
                MapTile.Enchanted_left()
            elif Keyword_input == '6':
                MapTile = MapTiles('Backward')
                MapTile.Enchanted_backward()
                print("Pick a number to go to that place")
                for Speacials in Speacial:
                    print(f"{Speacial.index(Speacials) + 1}. {Speacials}")
                # input for the CB
                Speacial_rooms_input = get_command("Place: ")
                if Speacial_rooms_input == '1':
                    MapTile = MapTiles('Belle')
                    MapTile.Conques_belle()
                    for Beasts in Beast:
                        print(f"{Beast.index(Beasts) + 1}. {Beasts}")
                    # input for the beast list and the beast room
                    Beast_room_input = get_command("Keyword: ")
                    if Beast_room_input == '1':
                        MapTile = MapTiles('Forward')
                        MapTile.Beast_forward()
                        break
                    elif Beast_room_input == '2':
                        MapTile = MapTiles('Right')
                        MapTile.Beast_right()
                    elif Beast_room_input == '3':
                        MapTile = MapTiles('Left')
                        MapTile.Beast_left()
                    else:
                        print("Invalid Direction")
            elif Keyword_input == '7':
                MapTile = MapTiles('Left')
                MapTile.Sherwood_left()
            elif Keyword_input == '8':
                MapTile = MapTiles('Backward')
                MapTile.Sherwood_backward()
            else:
                print("Invalid Direction")
        except NameError:
            print("You spelled the name wrong. Try again!")


# RAPUNZEL Story
# Picking inputs by the player
Input1 = ['Anyone there?', 'Can anyone hear me?', 'Quit']
Input2 = ["I will help you, come down.", "We can find them together", "Quit"]
Input3 = ["Come on let's go in", "You never know, come on.", "Quit"]
Input4 = ['Yess we did it Rapunzel!! Where can we find them?',
          'Perfect! where do they live?', 'Quit']
Input6 = ['Good Evening, Your Majesty', 'Hello, King and Queen', 'Quit']
Input7 = ['Quit', 'She is your daughter', 'Look at the similarities']
Input8 = ['Quit', 'Bye']
Place = ['Market', 'Church', 'Old Homes', 'New Homes']


def play1():
    """Game play for the Rapunzel story"""
    print("Tangled")
    print("""
In a far away tower, lived a beautiful princess named Rapunzel, but she had
no clue that she was a princess. She was taken from her parents by Mother
Gothel when she was born. Even since then, Rapunzel has been locked in a
tower. All she wants to do is to be free and find her parents.""")
    print("You are at the bottom of the tower and don't know anyone around.")
    # input when you meet rapunzel
    for Inputs1 in Input1:
        print(f"Inputs: {Inputs1}")
    answer_input = get_command("Response: ")
    for answer_input in Input1:
        if answer_input == 'Quit':
            sys.exit()
        elif answer_input == 'Anyone there?'or 'Can anyone hear me?':
            print("""
From the top of the tower, Rapunzel hears you and answers back.
RAPUNZEL: Who are you? Where are you from? I can't help you because I am
          locked in this tower. You might wonder why and I wish I could
          tell you, but I don't know. I really want to find my parents,
          though. I have never seem them.""")
            # input for talking to rapunzel
            for Inputs2 in Input2:
                print(f"Inputs: {Inputs2}")
            answer_input = get_command("Response: ")
            for answer_input in Input2:
                if answer_input == 'Quit':
                    sys.exit()
                elif answer_input == "I will help you, come down" or "We can find them together":
                    print("""
RAPUNZEL: Alright! I am coming down.
After she comes down, both of you continue on your path. Walking along a path,
both of you look around to find clues. You find a Tavern and ask Rapunzel to
come in with you.""")
                    # input for convincing rapunzel to go into tavern
                    for Inputs3 in Input3:
                        print(f"Inputs: {Inputs3}")
                    answer_input = get_command("Response: ")
                    for answer_input in Input3:
                        if answer_input == 'Quit':
                            sys.exit()
                        elif answer_input == "Come on let's go in" or "You never know what we will find, come on.":
                            print("""
RAPUNZEL: But I don't think we will find anything here because it is a
          tavern. Annyway, I will come along because there might be a
          chance.
They both enter the tavern just to get stared at by a bunch of drunk
viking thugs.
VIKING 1: Who are you?
VIKING 2: What are you doing here?
RAPUNZEL: I am sorry for intruding, but we were wondering if you can give us
          some information. I have lost my parents when I was just a little
          girl & I was taken away by Mother Gothel, who locked me away in a
          tower. I'm looking for my parents, so do you know anything.
VIKING 1: We have this picture if it helps. The viking hands the picture
          to Rapunzel, who looks stunned.
VIKING 2: Is this it?
Rapunzel: Ya! This is it!! That is me.""")
                            # input for finding the map of corona
                            for Inputs4 in Input4:
                                print(f"Inputs: {Inputs4}")
                            answer_input = get_command("Response: ")
                            for answer_input in Input4:
                                if answer_input == 'Quit':
                                    sys.exit()
                                elif answer_input == 'Perfect! Where are they?' or 'Yess we did it Rapunzel!! Where can we find them?':
                                    print("""
VIKING 1: They live in Corona. Did you know that you are the daughter of
          King Frederic and Queen Arianna.
RAPUNZEL: What?! I'm a PRINCESS! How do we go there?
VIKING 2: Keep going straight and you will see a bridge. You have to
          cross the bridge to get to Corona.
And so you and Rapunzel came out of the tavern and continued on their
path. After awhile, you see the bridge, so both cross the bidge.
When Rapunzel saw a stranger in the town of Corona, she went up to
them and started to question.
RAPUNZEL: Hi! Do you know where I can find my parents... I mean
King Frederick and Queen Arianna?
STRANGER: I am not sure, but check the homes. Here is a map.
RAPUNZEL: Thank you so much!! """)
                                    # printing the map here
                                    Mapss = Map1("Corona Map")
                                    Mapss.printing_maps()
                                    # Moving on the map of Corona
                                    tiles_moving1()


def tiles_moving1():
    """The function to show how to move from one place to another"""
    for Places in Place:
        print(f"- {Places}")
    while True:
        # input for the PLace list in COrona
        Place_input = get_command("Keyword: ")
        if Place_input == "Market":
            print("""They're not here. Check the homes.""")
        elif Place_input == "Church":
            print("""They're not here. Check the homes.""")
        elif Place_input == "Old Homes":
            print("""They're not here. Check the new homes.
There is a rumor that the New homes are getting a ceremony, so you will find
them there.""")
        elif Place_input == "New Homes":
            print("""The ceremony is going on right now, so you shouldn't
disturb them. Wait till the ceremony is done.
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
The ceremony has come to an end. You can go up to them now.""")
            # pick input when talking to King and queen
            for Inputs6 in Input6:
                print(f"Inputs: {Inputs6}")
            answer_input = get_command("Response: ")
            if answer_input == 'Quit':
                sys.exit()
            elif answer_input == 'Good Evening, Your Majesty'or 'Hello, King and Queen':
                print("""
KING: Good Evening, May I know Who you are?
Rapunzel slowly pulls out the picture when she was little and shows it
to the King and the Queen. After a long stare at the picture, they both
look back at Rapunzel.""")
                for Inputs7 in Input7:
                    print(f"Inputs: {Inputs7}")
                answer_input = get_command("Response: ")
                if answer_input == 'Quit':
                    sys.exit()
                elif answer_input == 'She is your daughter' or 'Look at the similarities':
                    print("""
QUEEN: My daughter! Oh my my!! You are Rapunzel, my daughter!!!
RAPUNZEL: Mom. Mom, I'm so glad I'm here.
KING: Rapunzel, so are we, my darling.
Rapunzel and her family lived happily ever after!""")
                    # inputs for exiting the game
                    for Inputs8 in Input8:
                        print(f"Inputs: {Inputs8}")
                    answer_input = get_command("Response: ")
                    for answer_input in Input8:
                        if answer_input == 'Quit':
                            sys.exit()
                        elif answer_input == 'Bye':
                            print("The End")


def get_command(message):
    """making the input captial for some"""
    # defining player inputs
    # making a try-except statement to be error-free
    try:
        action_input = input(message)
        return action_input.title()
        answer_input = input(message)
        return answer_input.title()
        Place_input = input(message)
        return Place_input.title()
        game_input = input(message)
        return game_input
    except NameError:
        print("You spelled the name wrong. Try again!")


def game_choice():
    """Input for picking a Game"""
    print("Land of Fairy Tales")
    print("Choose a game to start:")
    for game in Games:
        print(f"{Games.index(game) + 1}. {game.title()}")
    while True:
        game_input = get_command("Game: ")
        if game_input == '1':
            play()
        elif game_input == '2':
            play1()
        else:
            print("Invalid Input")


game_choice()

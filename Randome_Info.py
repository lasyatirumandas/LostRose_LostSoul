# random info

def choose_Enchanted_Forest():
    """Function for what happens and your chooses in Enchanted Forest"""
    print("You are in the Enchanted forest and you have found a sword on the")
    print("ground and now that is yours.")
    # Options for direction input and what happens in each direction
    print(Directions)
    while True:
        # making a try-except statement to be error-free
        try:
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
                    # option for place input to go to another place
                    Classes.tiles_moving()
            else:
                print("Invalid Direction")
        except NameError:
            print("You spelled the name wrong. Try again!")


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
        if action_input == 'Quit':
            sys.exit()
        # option for place input to go to another place
        elif action_input == 'Places':
            Classes.tiles_moving()
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
        # making a try-except statement to be error-free
        try:
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
                    print("The beast awakes with the sound of your footsteps")
                    print("ROBIN: I will deal with him, you go put the Rose.")
                # this shows what happens when forward option
                elif direction_input == 'Forward':
                    print(f"Moving Forward")
                    print("You found the case to put the rose before Beast")
                    print("comes closer. The beast restores into human form.")
                    print("You did it!!! Success")
                elif direction_input == 'Quit':
                    sys.exit()
                # option for place input to go to another place
                elif direction_input == 'Places':
                    Classes.tiles_moving()
            else:
                print("Invalid Direction")
        except NameError:
            print("You spelled the name wrong. Try again!")


Classes.tiles_moving() 

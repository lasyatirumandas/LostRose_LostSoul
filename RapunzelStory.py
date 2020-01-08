from Map import Map1
import sys

# Picking inputs by the player
Input1 = ['Anyone there?', 'Can anyone hear me?', 'Quit']
Input2 = ["I will help you, come down.", "We can find them together",
          "Quit"]
Input3 = ["Come on let's go in", "You never know, come on.", "Quit"]
Input4 = ['Yess we did it Rapunzel!! Where can we find them?',
          'Perfect! where do they live?', 'Quit']
Input6 = ['Good Evening, Your Majesty', 'Hello, King and Queen', 'Quit']
Input7 = ['Quit', 'She is your daughter', 'Look at the similarities']
Input8 = ['Quit', 'Bye']
Place = ['Market', 'Church', 'Old Homes', 'New Homes']


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
                print("""KING: Good Evening, May I know Who you are?
                      Rapunzel slowly pulls out the picture when she was
                      little and shows it to the King and the Queen.
                      After a long stare at the picture, they both look
                      back at Rapunzel.""")
                for Inputs7 in Input7:
                    print(f"Inputs: {Inputs7}")
                answer_input = get_command("Response: ")
                if answer_input == 'Quit':
                    sys.exit()
                elif answer_input == 'She is your daughter' or 'Look at the similarities':
                    print("""QUEEN: My daughter! Oh my my!! You are
                                    Rapunzel, my daughter!!!
                             RAPUNZEL: Mom. Mom, I'm so glad I'm here.
                             KING: Rapunzel, so are we, my darling. """)
                    print("""Rapunzel and her family lived happily ever after!
                    """)
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
    """making the input captial"""
    # making a try-except statement to be error-free
    try:
        Place_input = input(message)
        return Place_input.title()
    except NameError:
        print("You spelled the name wrong. Try again!")


def play1():
    """Game play for the Rapunzel story"""
    print("""In a far away tower, lived a beautiful princess named Rapunzel,
          but she had no clue that she was a princess. She was taken from her
          parents by Mother Gothel when she was born. Even since then,
          Rapunzel has been locked in a tower. All she wants to do is to be
          free and find her parents.
          """)
    print("You are at the bottom of the tower and don't know anyone around.")
    # input when you meet rapunzel
    for Inputs1 in Input1:
        print(f"Inputs: {Inputs1}")
    answer_input = get_command("Response: ")
    for answer_input in Input1:
        if answer_input == 'Quit':
            sys.exit()
        elif answer_input == 'Anyone there?'or 'Can anyone hear me?':
            print("""From the top of the tower, Rapunzel hears you
                     and answers back.
                     RAPUNZEL: Who are you? Where are you from? I can't
                            help you because I am locked in this tower.
                            You might wonder why and I wish I could tell
                            you, but I don't know. I really want to find
                            my parents, though. I have never seem them.""")
            # input for talking to rapunzel
            for Inputs2 in Input2:
                print(f"Inputs: {Inputs2}")
            answer_input = get_command("Response: ")
            for answer_input in Input2:
                if answer_input == 'Quit':
                    sys.exit()
                elif answer_input == "I will help you, come down" or "We can find them together":
                    print("""RAPUNZEL: Alright! I am coming down.""")
                    print("""After she comes down, both of you continue on
                          your path.
                          Walking along a path, both of you look around to
                          find clues. You find a Tavern and ask Rapunzel to
                          come in with you.""")
                    # input for convincing rapunzel to go into tavern
                    for Inputs3 in Input3:
                        print(f"Inputs: {Inputs3}")
                    answer_input = get_command("Response: ")
                    for answer_input in Input3:
                        if answer_input == 'Quit':
                            sys.exit()
                        elif answer_input == "Come on let's go in" or "You never know what we will find, come on.":
                            print("""RAPUNZEL: But I don't think we will find
                                               anything here because it is a
                                               tavern. Annyway, I will come
                                               along because there might be a
                                               chance.""")
                            print("""They both enter the tavern just to get
                                  stared at by a bunch of drunk viking thugs.
                                  VIKING 1: Who are you?
                                  VIKING 2: What are you doing here?
                                  RAPUNZEL: I am sorry for intruding, but we
                                            were wondering if you can give us
                                            some information. I have lost my
                                            parents when I was just a little
                                            girl & I was taken away by Mother
                                            Gothel, who locked me away in a
                                            tower. I'm looking for my parents
                                            and I was wondering if you knew
                                            anyone.
                                  VIKING 1: We have this picture if it helps.
                                  The viking hands the picture to Rapunzel,
                                  who looks stunned.
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
                                    print("""VIKING 1: They live in Corona.
                                                       Did you know that you
                                                       are the daughter of
                                                       King Frederic and
                                                       Queen Arianna.
                                             RAPUNZEL: What?! I'm a PRINCESS!
                                                       How do we go there?
                                             VIKING 2: Keep going straight
                                                       and you will see a
                                                       bridge. You have to
                                                       cross the bridge to
                                                       get to Corona.""")
                                    print("""And so you and Rapunzel came out
                                          of the tavern and continued on
                                          their path.
                                          After awhile, you see the bridge,
                                          so you and Rapunzel cross the bidge.
                                          """)
                                    print("""When Rapunzel saw a stranger in
                                          the town of Corona, she went up to
                                          them and started to question.
                                          RAPUNZEL: Hi! Do you know where I
                                                    can find my parents... I
                                                    mean King Frederick and
                                                    Queen Arianna?
                                          STRANGER: I am not sure exactly
                                                    where they would be, but
                                                    check the homes.
                                                    Here is a map.
                                          RAPUNZEL: Thank you so much!!
                                          """)
                                    # printing the map here
                                    Mapss = Map1("Corona Map")
                                    Mapss.printing_maps()
                                    # Moving on the map of Corona
                                    tiles_moving1()


def get_command(message):
    """making the input captial"""
    # making a try-except statement to be error-free
    try:
        answer_input = input(message)
        return answer_input.title()
    except NameError:
        print("You spelled the name wrong. Try again!")


# calling the function to excute the game
play1()

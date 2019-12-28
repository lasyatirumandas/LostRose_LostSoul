from Map import Map1
import sys

# Pick an input for 'anyone there'
Input1 = ['Anyone there?', 'Can anyone hear me?', 'exit']
Input2 = ["I will help you, come down.", "We can find them together",
          "exit"]
Input3 = ["Come on let's go in", "You never know, come on.", "exit"]
Input4 = ['Yess we did it Rapunzel!! Where can we find them?',
          'Perfect! where do they live?', 'exit']
Input5 = ["Hey! There's a store and I'm going to go to buy food, come along?",
          "Rpaunzel, come on! Let's go get food", "exit"]

def play1():
    """Game play for the Rapunzel story"""
    print("""In a far away tower, lived a beautiful princess named Rapunzel,
          but she had no clue that she was a princes. She was taken from her
          parents by Mother Gothel when she was born. Even since then,
          Rapunzel has been locked in a tower. All she wants to do is to be
          free and find her parents.
          """)
    print("You are at the bottom of the tower and don't know anyone around.")
    for Inputs1 in Input1:
        print(f"- Inputs")
    answer_input = get_command("Response: ")
    for answer_input in Input1:
        if answer_input == 'Anyone there?'or 'Can anyone hear me?':
            print("""From the top of the tower, Rapunzel hears you
                     and answers back.
                     RAPUNZEL: Who are you? Where are you from? I can't
                            help you because I am locked in this tower.
                            You might wonder why and I wish I could tell
                            you, but I don't know. I really want to find
                            my parents, though. I have never seem them.""")
        elif answer_input == 'Quit':
             sys.exit()
        else:
             print("Invalid Action")
            for Inputs2 in Input2:
                print(f"- Inputs")
            answer_input = get_command("Response: ")
            for answer_input in Input2:
                if answer_input == 'I will help you, come down.'
                                    or 'We can find them together':
                    print("""RAPUNZEL: Alright! I am coming down.""")
                    print("""After she comes down, both of you continue on
                          your path.
                          Walking along a path, both of you look around to
                          find clues. You find a Tavern and ask Rapunzel to
                          come in with you.""")
                elif answer_input == 'Quit':
                    sys.exit()
                else:
                    print("Invalid Action")
                    for Inputs3 in Input3:
                        print(f"- Inputs")
                    answer_input = get_command("Response: ")
                    for answer_input in Input3:
                        if answer_input == "Come on let's go in" or
                                "You never know what we will find, come on.":
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
                         elif answer_input == 'Quit':
                             sys.exit()
                         else:
                             print("Invalid Action")
                            for Inputs4 in Input4:
                                print(f"- Inputs")
                            answer_input = get_command("Response: ")
                            for answer_input in Input4:
                                if answer_input == 'Perfect! Where are they?'
                     or 'Yess we did it Rapunzel!! Where can we find them?':
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
                                          After o long, you see the bridge 
                                          and you and Rapunzel cross the bidge.
                                          """)
                                  elif answer_input == 'Quit':
                                      sys.exit()
                                  else:
                                      print("Invalid Action")
                                    # printing the map here
                                    Mapss = Map1("Corona Map")
                                    print(Mapss.printing_maps())

                                    

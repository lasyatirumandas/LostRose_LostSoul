# Lasya Tirumandas
# CS30 P1
# Dec 2, 2019
# RPG Class

# list of places to move to
Keyword = ['EF', 'ER', 'SF', 'SR', 'EL', 'EB', 'SL', 'SB']
Beast = ['BF', 'BR', 'BL']
Speacial_room = ['CB']


def tiles_moving():
    """The function to show how to move from one place to another"""
    for Keywords in Keyword:
        print(f"- {Keywords}")
    while True:
        # input for the keyword list
        Keyword_input = get_command("Keyword: ")
        try:
            if Keyword_input == 'EF':
                MapTile = MapTiles('Forward')
                MapTile.Enchanted_forward()
            elif Keyword_input == 'ER':
                MapTile = MapTiles('Right')
                MapTile.Enchanted_right()
            elif Keyword_input == 'SF':
                MapTile = MapTiles('Forward')
                MapTile.Sherwood_forward()
            elif Keyword_input == 'SR':
                MapTile = MapTiles('Right')
                MapTile.Sherwood_right()
            elif Keyword_input == 'EL':
                MapTile = MapTiles('Left')
                MapTile.Enchanted_left()
            elif Keyword_input == 'EB':
                MapTile = MapTiles('Backward')
                MapTile.Enchanted_backward()
                for Speacial_rooms in Speacial_room:
                    print(f"- {Speacial_rooms}")
                # input for the CB
                Speacial_rooms_input = get_command("Place: ")
                if Speacial_rooms_input == 'CB':
                    MapTile = MapTiles('Belle')
                    MapTile.Conques_belle()
                    for Beasts in Beast:
                        print(f"- {Beasts}")
                    # input for the beast list and the beast room
                    Beast_room_input = get_command("Keyword: ")
                    if Beast_room_input == 'BF':
                        MapTile = MapTiles('Forward')
                        MapTile.Beast_forward()
                        break
                    elif Beast_room_input == 'BR':
                        MapTile = MapTiles('Right')
                        MapTile.Beast_right()
                    elif Beast_room_input == 'BL':
                        MapTile = MapTiles('Left')
                        MapTile.Beast_left()
                    else:
                        print("Invalid Direction")
            elif Keyword_input == 'SL':
                MapTile = MapTiles('Left')
                MapTile.Sherwood_left()
            elif Keyword_input == 'SB':
                MapTile = MapTiles('Backward')
                MapTile.Sherwood_backward()
            else:
                print("Invalid Direction")
        except:
            print("Invalid input")


def get_command(message):
    """making the input captial"""
    try:
        Keyword_input = input(message)
        return Keyword_input
        Beast_room_input = input(message)
        return Beast_room_input
        Speacial_rooms_input = input(message)
        return Speacial_rooms_input
    except NameError:
        print("You spelled the name wrong. Try again!")


class MapTiles:
    """This is the class for the different locations in the game"""
    def __init__(self, locations):
        self.locations = locations

    def Enchanted_forward(self):
        """This is the function for Enchanted_forward tile"""
        print(f""" Going {self.locations}.
        There is nothing here.""")

    def Enchanted_right(self):
        """This is the function for Enchanted_right tile"""
        print(f""" Going {self.locations}.
        The orge is sleeping and you will let it sleep.
        """)

    def Enchanted_left(self):
        """This is the function for Enchanted_left tile"""
        print(f""" Going {self.locations}.
        There is nothing here.""")

    def Enchanted_backward(self):
        """This is the function for Enchanted_backward tile"""
        print(f""" Going {self.locations}.
        You found the rose.""")

    def Sherwood_forward(self):
        """This is the function for Sherwood_forward tile"""
        print(f""" Going {self.locations}.
        There is nothing here.""")

    def Sherwood_right(self):
        """This is the function for Sherwood_right tile"""
        print(f""" Going {self.locations}.
        There is nothing here.""")

    def Sherwood_backward(self):
        """This is the function for Sherwood_backward tile"""
        print(f""" Going {self.locations}.
        There is nothing here.""")

    def Sherwood_left(self):
        """This is the function for Sherwood_left tile"""
        print(f""" Going {self.locations}.
        Robin Hood greets you.
        Robin Hood and you have become alliances in this adventure.
        ROBIN: I heard from Belle that you need assistance with something
        and I will help you hold off the beast and I am willing to come
        with you.
        You hear villagers whispering about the red rose.
        And listening to their conversation, you realize that it is the
        Rose you are looking for.
        VILLAGERS: I heard that the red rose to heal the beast is in the
        Enchanted forest.
        ROBIN: Let's go to the Enchanted Forest.
        """)

    def Conques_belle(self):
        """This is the function for Conques_belle tile"""
        print(f""" Going {self.locations}.
        You are in France.
        BELLE: Did you find the rose?
        ROBIN: Yes yes we did!
        BELLE: That's amazing!
        ROBIN: We should hurry to the beast now and i will come with u.
        BELLE: Boys get your weapons ready.
        BELLE: There he is....
        This is the Beast room.
        """)

    def Beast_forward(self):
        """This is the function for Beast_forward tile"""
        print(f""" Going {self.locations}.
        You found the case to put the rose before the beast
        comes closer. The beast restores into human form, now.
                        The End!!
        """)

    def Beast_right(self):
        """This is the function for Beast_right tile"""
        print(f""" Going {self.locations}.
        You can hear the growls louder and make out a
        figure from the dark.
        The beast awakes with the sound of your footsteps.
        ROBIN: Hey I will deal with him, you go put the Rose.
        """)

    def Beast_left(self):
        """This is the function for Beast_left tile"""
        print(f""" Going {self.locations}.
        There is nothing here.""")


# call the function to execute the game
# tiles_moving()

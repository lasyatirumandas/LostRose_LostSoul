# Lasya Tirumandas
# CS30 P1
# Dec 2, 2019
# RPG Class

Keyword = ['EF', 'ER', 'SF', 'SR', 'EL', 'EB', 'SL', 'SB', 'CB']
Beast = ['BF','BR', 'BL']

def tiles_moving():
    """The function to show how to move from one place to another"""
    for Keywords in Keyword:
        print(f"- {Keywords}")
    while True:
        Keyword_input = get_command("Keyword: ")
        for Keyword_input in Keyword:
            if Keyword_input == 'EF':
                MapTile = EF('Forward')
                print(MapTile.Enchanted_forward())
            elif Keyword_input == 'ER':
                MapTile = ER('Right')
                print(MapTile.Enchanted_right())
            elif Keyword_input == 'SF':
                MapTile = SF('Forward')
                print(MapTile.Sherwood_forward())
            elif Keyword_input == 'SR':
                MapTile = SR('Right')
                print(MapTile.Sherwood_right())
            elif Keyword_input == 'EL':
                MapTile = EL('Left')
                print(MapTile.Enchanted_left())
            elif Keyword_input == 'EB':
                MapTile = EB('Backward')
                print(MapTile.Enchanted_backward())
            elif Keyword_input == 'SL':
                MapTile = SL('Left')
                print(MapTile.Sherwood_left())
            elif Keyword_input == 'SB':
                MapTile = SB('Backward')
                print(MapTile.Sherwood_backward())
            elif Keyword_input == 'CB':
                MapTile = CB('Belle')
                print(MapTile.Conques_belle())
                for Beasts in Beast:
                    print(f"- {Beasts}")
                Beast_room_input = get_command("Keyword: ")
                for Beast_room_input in Beast:
                    if Beast_room_input == 'BF':
                        MapTile = BF('Forward')
                        print(MapTile.Beast_forward())
                    elif Beast_room_input == 'BR':
                        MapTile = BR('Right')
                        print(MapTile.Beast_right())
                    elif Beast_room_input == 'BL':
                        MapTile = BL('Left')
                        print(MapTile.Beast_left())
                    else:
                        print("Invalid Direction")
            else:
                print("Invalid Direction")


def get_command(message):
    """making the input captial"""
    Keyword_input = input(message)
    return Keyword_input.title()

class MapTiles:
    def __init__(self, locations):
        self.locations = locations


    def Starting_Point(self):
        print(f""" {self.locations}.
        Hi! I am Belle. The love of my life has been a Beast and will stay
        as a Beast if you don't find the Rose, which will restore him into
        a charming Prince, that he was once.
        And You will help me restore my Beast.
        There are three places that you can visit and in one of these
        places, you will find the Rose.
        I have already informed Robin Hood about your arrival and he
        will be waiting for you in Sherwood Forest.
        Right now, you are in Conques, France.
        Please come back here when you find the Rose.""")

class EF(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Enchanted_forward(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")

class ER(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Enchanted_right(self):
        print(f""" Going {self.locations}.
        The orge is sleeping and you will let it sleep.
        """)


class EL(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Enchanted_left(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")


class EB(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Enchanted_backward(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")


class SF(MapTiles):
    def __init__(self, locations):
        self.locations = locations
    def Sherwood_forward(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")


class SR(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Sherwood_right(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")


class SB(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Sherwood_backward(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")


class SL(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Sherwood_left(self):
        print(f""" Going {self.locations}.
        You are in the Sherwood forest and Robin Hood greets you.
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


class CB(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Conques_belle(self):
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


class BF(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Beast_forward(self):
        print(f""" Going {self.locations}.
        You found the case to put the rose before the beast
        comes closer. The beast restores into human form, now.
        """)


class BR(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Beast_right(self):
        print(f""" Going {self.locations}.
        You can hear the growls louder and make out a
        figure from the dark.
        The beast awakes with the sound of your footsteps.
        ROBIN: Hey I will deal with him, you go put the Rose.
        """)


class BL(MapTiles):
    def __init__(self, locations):
        self.locations = locations

    def Beast_left(self):
        print(f""" Going {self.locations}.
        There is nothing here.""")


tiles_moving()

# Lasya Tirumandas
# CS30 P1
# Dec 2, 2019
# RPG Class

Keyword = ['EF', 'ER', 'SF', 'SR', 'EL', 'EB', 'SL', 'SB', 'CB', 'BF',
           'BR', 'BL', 'BB'
           ]

def tiles_moving():
    """The function to show how to move from one place to another"""
    for Keywords in Keyword:
        print(f"- {Keywords}")
    while True:
        Keyword_input = get_command("Keyword: ")
        for Keyword_input in Keyword:
            if Keyword_input == 'EF':
                Enchanted_forward.locations()
                Enchanted_forward.description()

def get_command(message):
    """making the input captial"""
    Keyword_input = input(message)
    return Keyword_input.title()

class MapTiles:
    def __init__(self, locations):
        self.locations = locations

    def __str__(self):
        return self.description


class Starting_point(MapTiles):
    def __init__(self, locations):
        self.locations = "Start"
        self.description = """
        Hi! I am Belle. The love of my life has been a Beast and will stay
        as a Beast if you don't find the Rose, which will restore him into
        a charming Prince, that he was once.
        And You will help me restore my Beast.
        There are three places that you can visit and in one of these
        places, you will find the Rose.
        I have already informed Robin Hood about your arrival and he
        will be waiting for you in Sherwood Forest.
        Right now, you are in Conques, France.
        Please come back here when you find the Rose.
        """


class Enchanted_forward(MapTiles):
    def __init__(self, locations):
        self.locations = "Forward"
        self.description = """
        There is nothing here
        """


class Enchanted_right(MapTiles):
    def __init__(self, locations):
        self.locations = "Right"
        self.description = """
        The orge is sleeping and you will let it sleep.
        """


class Enchanted_left(MapTiles):
    def __init__(self, locations):
        self.locations = "Left"
        self.description = """
        There is nothing here
        """


class Enchanted_backward(MapTiles):
    def __init__(self, locations):
        self.locations = "Backward"
        self.description = """
        There is nothing here
        """


class Sherwood_forward(MapTiles):
    def __init__(self, locations):
        self.locations = "Forward"
        self.description = """
        There is nothing here
        """


class Sherwood_right(MapTiles):
    def __init__(self, locations):
        self.locations = "Right"
        self.description = """
        There is nothing here
        """


class Sherwood_backward(MapTiles):
    def __init__(self, locations):
        self.locations = "Backward"
        self.description = """
        There is nothing here
        """


class Sherwood_left(MapTiles):
    def __init__(self, locations):
        self.locations = "Left"
        self.description = """
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
        """


class Conques_belle(MapTiles):
    def __init__(self, locations):
        self.locations = "Conques"
        self.description = """
        You are in France.
        BELLE: Did you find the rose?
        ROBIN: Yes yes we did!
        BELLE: That's amazing!
        ROBIN: We should hurry to the beast now and i will come with u.
        BELLE: Boys get your weapons ready.
        BELLE: There he is....
        This is the Beast room.
        """


class Beast_forward(MapTiles):
    def __init__(self, locations):
        self.locations = "Forward"
        self.description = """
        You found the case to put the rose before the beast
        comes closer. The beast restores into human form, now.
        """


class Beast_right(MapTiles):
    def __init__(self, locations):
        self.locations = "Right"
        self.description = """ You can hear the growls louder and make out a
        figure from the dark.
        The beast awakes with the sound of your footsteps.
        ROBIN: Hey I will deal with him, you go put the Rose.
        """


class Beast_left(MapTiles):
    def __init__(self, locations):
        self.locations = "Left"
        self.description == """
        There is nothing here
        """


tiles_moving()

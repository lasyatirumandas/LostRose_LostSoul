# Lasya Tirumandas
# CS30 P1
# Dec 2, 2019
# RPG Class


 class MapTile:
     def __init__(self, x, y):
         self.x = x
         self.y = x
         self.Locations


class Starting_point(MapTile):
    def Starting_point(self):
        self.Locations = Starting_point
        return """
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


class Enchnated_forward(MapTiles):
    def Enchnated_forward(self):
        self.Locations = Enchnated_forward
        return """
        There is nothing here
        """


class Enchanted_right(MapTiles):
    def Enchanted_right(self):
        self.Locations = Enchanted_right
        return """
        The orge is sleeping and you will let it sleep.
        """


class Enchanted_left(MapTiles):
    def Enchanted_left(self):
        self.Locations = Enchanted_left
        return """
        There is nothing here
        """


class Enchanted_backward(MapTiles):
    def Enchanted_backward(self):
        self.Locations = Enchanted_backward
        return """
        There is nothing here
        """


class Sherwood_forward(MapTiles):
    def Sherwood_forward(self):
        self.Locations = Sherwood_forward
        return """
        There is nothing here
        """


class Sherwood_right(MapTiles):
    def Sherwood_right(self):
        self.Locations = Sherwood_right
        return """
        There is nothing here
        """


class Sherwood_backward(MapTiles):
    def Sherwood_backward(self):
        self.Locations = Sherwood_backward
        return """
        There is nothing here
        """


class Sherwood_left(MapTiles):
    def Sherwood_left(self):
        self.Locations = Sherwood_left
        return """
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
    def Conques_belle(self):
        self.location = Conques_belle
        return """You are in France.
        BELLE: Did you find the rose?
        ROBIN: Yes yes we did!
        BELLE: That's amazing!
        ROBIN: We should hurry to the beast now and i will come with u.
        BELLE: Boys get your weapons ready.
        BELLE: There he is....
        This is the Beast room.
        """


class Beast_forward(MapTiles):
    def Beast_forward(self):
        self.location = Beast_forward
        return """You found the case to put the rose before the beast
        comes closer. The beast restores into human form, now.
        """


class Beast_right(MapTiles):
    def Beast_right(self):
        self.location = Beast_right
        return """You can hear the growls louder and make out a
        figure from the dark.
        The beast awakes with the sound of your footsteps.
        ROBIN: Hey I will deal with him, you go put the Rose.
        """


class Beast_left(MapTiles):
    def Beast_left(self):
        self.location = Beast_left
        return """Nothing is here
        """


class Beast_left(MapTiles):
    def Beast_left(self):
        self.location = Beast_left
        return """Nothing is here
        """


class Nothing_Space1(MapTiles):
    def Nothing_Space1(self):
        self.location = Nothing_Space1
        return """Nothing is here
        """


class Nothing_Space2(MapTiles):
    def Nothing_Space2(self):
        self.location = Nothing_Space2
        return """Nothing is here
        """

# Lasya Tirumandas
# CS30 P1
# Nov 18, 2019
# Map

# Make a list of all the places on the map
land_map = [
            ['Enchanted_forward', 'Enchanted_right', 'Sherwood_forward',
             'Sherwood_right'],
            ['Enchanted_left', 'Enchanted_backward', 'Sherwood_left',
             'Sherwood_backward'],
            ['starting point', 'Conques_belle', 'Beast_forward',
             'Beast_right'],
            [' Nothing_Space1', 'Nothing_Space2', 'Beast_left',
             'Beast_backward']
            ]


# make a function for printing the map
def land_maps():
    """Printing the map that looks above"""
    for rows in land_map:
        print(rows)


# printing Map
class ViewMap(MapTiles):
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

land_map = | E_F | E_R | S_F | S_R |
# showing layout of the lands
# land_map = [
#             [Enchanted_forward(0, 4), Enchanted_right(1, 4), Sherwood_forward(2, 4),
#              Sherwood_right(3, 4)],
#             [Enchanted_left(0, 3), Enchanted_backward(1, 3), Sherwood_left(2, 3),
#              Sherwood_backward(3, 3)],
#             [starting point(0, 2), Conques_belle(1, 2), Beast_forward(2, 2),
#              Beast_right(3, 2)],
#             [Nothing_Space1(0, 1), Nothing_Space2(1, 1), Beast_left(2, 1),
#              Beast_backward(3, 1)]
#             ]

# Print the land_map
print(land_maps())

# Lasya Tirumandas
# CS30 P1
# Nov 18, 2019
# Map

# Make a list of all the places on the map
# land_map = [
#             ['Enchanted_forward', 'Enchanted_right', 'Sherwood_forward',
#              'Sherwood_right'],
#             ['Enchanted_left', 'Enchanted_backward', 'Sherwood_left',
#              'Sherwood_backward'],
#             ['starting point', 'Conques_belle', 'Beast_forward',
#              'Beast_right'],
#             [' Nothing_Space1', 'Nothing_Space2', 'Beast_left',
#              'Beast_backward']
#             ]
#
#
# # make a function for printing the map
# def land_maps():
#     """Printing the map that looks above"""
#     for rows in land_map:
#         print(rows)
#
#
# # Print the land_map
# print(land_maps())

# showing layout of the lands
# land_map = [
#             [Enchanted_forward(0, 4), Enchanted_right(1, 4),
#              Sherwood_forward(2, 4), Sherwood_right(3, 4)],
#             [Enchanted_left(0, 3), Enchanted_backward(1, 3),
#              Sherwood_left(2, 3), Sherwood_backward(3, 3)],
#             [starting_point(0, 2), Conques_belle(1, 2),
#              Beast_forward(2, 2), Beast_right(3, 2)],
#             [Nothing_Space1(0, 1), Nothing_Space2(1, 1), Beast_left(2, 1),
#              Beast_backward(3, 1)]
#             ]


class Map:
    """create a map using class"""
    def __init__(self, print):
        """printing a map"""
        self.print = print

    def printing_map(self):
        """printing the map in the order i want it to be seen"""
        print(f""" {self.print}-
| Enchanted_forward(EF) | Enchanted_right(ER)    | Sherwood_forward(SF) | Sherwood_right(SR)    |
| Enchanted_left(EL)    | Enchanted_backward(EB) | Sherwood_left(SL)    | Sherwood_backward(SB) |
| starting_point(SP)    | Conques_belle(CB)      | Beast_forward(BF)    |   Beast_right(BR)     |
                                                 | Beast_left(BL)       | 
""")

# calling the fucntion to print the map
Maps = Map("Map")
print(Maps.printing_map())

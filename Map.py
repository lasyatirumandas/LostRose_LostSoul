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
            ['               ', 'Conques_belle', 'Beast_forward',
             'Beast_right'],
            ['               ', '             ', 'Beast_left',
             'Beast_backward']
            ]


# make a function for printing the map
def land_maps():
    """Printing the map that looks above"""
    for rows in land_map:
        print(rows)


# Print the land_map
print(land_maps())

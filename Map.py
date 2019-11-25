# Lasya Tirumandas
# CS30 P1
# Nov 18, 2019
# Map


land_map = [
        ['Enchanted_forward', 'Enchanted_right', 'Sherwood_forward', 'Sherwood_right'],
        ['Enchanted_left', 'Enchanted_backward', 'Sherwood_left', 'Sherwood_backward'],
        ['               ', 'Conques_belle', 'Beast_forward', 'Beast_right'],
        ['               ', '             ', 'Beast_left', 'Beast_backward']
]


def land_maps():
    for rows in land_map:
        print(rows)

print(land_maps())

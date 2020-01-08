# Lasya Tirumandas
# CS30 P1
# Dec 5, 2019
# Character


# Characters = ['Belle', 'Beast', 'Robin Hood', 'Villagers', 'You']
#
# def characters_in_game():
#     """Printing the characters that looks above"""
#     print('The charcaters in the game are:')
#     for rows in Characters:
#         print(rows)
#
# characters_in_game()


class Character:
    """Create characters list using class"""
    def __init__(self, print):
        """printing the characters"""
        self.print = print

    def printing_characters(self):
        """printing the characters in the order i want it to be seen"""
        print(f""" {self.print}-
        Belle
        Beast
        Robin Hood
        Villagers
        You
""")

# calling the fucntion to print the character names
# characters = Character("Character Names")
# characters.printing_characters()

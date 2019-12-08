# Lasya Tirumandas
# CS30 P1
# dec 5, 2019
# Character

# list of character anmes in the game
# Characters = ['Belle', 'Beast', 'Robin Hood', 'Villagers', 'You']


# def Character_in_game():
#   """Printing the characters from the above list"""
#   print('The Characters in the game are:')
#   for names in Charcaters:
#     print(names)
    

# # calling out the function to print character names
# characters_in_game()


class characters:
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
character = characters("Character Names")
print(character.printing_characters())

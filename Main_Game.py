# Lasya Tirumandas
# CS30 P1
# October 21, 2019
# Nested Dictionaries

# This is dictionary for Chaarcter and their description printed in for loop
Character = {
            'Belle': 'is selfless & is emotionally attached to the Beast',
            'Beast': 'turned from a charming Prince into a hideous Beast as a pusnishment for being cold-hearted and brutal',
            'Robin Hood': 'lives in Sherwood Forest & is a friend of Belle, so he can help you with the mission',
            'Villagers': 'live in Sherwood Forest & help you find the rose'
            }
print("             Characters:")
for name, info in Character.items():
    print(f"{name} {info}")
print("")


# THis is dictionary for Places and its description printed in for loop
Places = {
        'Enchanted Forest': 'In this location, you will fight a orge and you can look for the Rose',
        'Sherwood Forest': 'Here, you will meet Robin Hood, who will help you find the Rose and fight the Beast',
        'Conques': 'You will start your journey here & meet talk to Belle to find out information regards the Beast'
          }
print("             Places:")
for location, info in Places.items():
    print(f"{location}- {info}")
print("")


# This is nested dictionary for items and its descriptions in for loop
Items = {
        'Rose': {'Uses': 'can restore the beast', 'Symbolizes': 'pure heart of the beast'},
        'Robin Bow': {'Uses': 'to fight the beast', 'Symbolizes': 'power of unity'},
        'Swords': {'Uses': 'to fight the beast', 'Symbolizes': 'strenght within you'}
        }
print("             Inventory:")
for item, item_info in Items.items():
    print(f"Item: {item}")
    use = item_info['Uses']
    symbol = item_info['Symbolizes']
    print(f"\tUses: {use}")
    print(f"\tSymbolizes: {symbol}")

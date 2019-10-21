# Lasya Tirumandas
# CS30 P1
# October 21, 2019
# Nested Dictionaries


# Character = ['Belle', 'Beast', 'Robin Hood', 'Villagers']
# Items_To_Be_Found = ['Rose', 'Magic Bean', 'Robin bow', 'Swords']
# Places = ['Enchanted Forest', 'Sherwood Forest', 'Conques, France']

Character = {'Belle': 'is selfless & is emotionally attached to the Beast',
            'Beast': 'turned from a charming Prince into a hideous Beast as a pusnishment for being cold-hearted and brutal',
            'Robin Hood': 'lives in Sherwood Forest & is a friend of Belle, so he can help you with the mission',
            'Villagers': 'live in SHerwood Forest & help you find the rose'
            }
for name, info in Character.items():
    print(f"{name} {info}")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")


Places = {'Enchanted Forest': 'In this location, you will fight a orge and you can look for the Rose ',
        'Sherwood Forest': 'Here, you will meet Robin Hood, who will help you find the Rose and fight the Beast',
        'Conques': 'You will start your journey here & meet talk to Belle to find out information regards the Beast'
        }
for location, info in Places.items():
    print(f"{location}- {info}")


Inventory = {'Items': {'Rose':'', 'Magic Bean': '', 'Robin Bow': '', 'Swords': ''}}

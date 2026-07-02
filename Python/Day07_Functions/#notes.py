#notes
#FUNCTIONS

#we can define a function using the def keyword.
def nothing():
    pass  # if we would want to pass a function without any code, we can use the pass keyword and use the func it for later.
print(nothing())
print()
def hello_function():
    print("Hello function")
hello_function()          #pretty self explanatory just use ur brain
print()
def boss_function():
    print("I am the boss!") #just change this to anything u want for the explanation below.

boss_function() #alright so lets say our boss wants us to print a certain string a number of times
boss_function() #and the boss wants to change a single word or symbol in the strings,
boss_function() #instead of rewriting the whole string we can just change the function

#fun fact ^ is called DRY, which is dont repeat yourself basically for new people that dont know they could just
#put stuff in variables isntead of making it more complex

#RETURNING VALUES
#now functions can also be returned basically makes it if you want to print out a function you have
#to type print(function_name()) instead of just function_name()
#and u might be thinking aint this just complicating it, now theres a gooood use to it
#without the return value the function only can be executed by its own
#but with the return value we can treat it as a normal string and put it into more complex functions
print()
def return_function():
    return "I am a return function"
print(return_function())
# now we can use more ways with this function like using .upper and .lower
print(return_function().upper())
print()

                    #now we can return functions + formatting anything to the function byy doing this
def bro(greeting):
    return '{} bro!'.format(greeting)
print(bro('Whats up'))              #like this you can use f' instead of .format btw
print()

                                # we can also put more than just a greeting by adding a comma,
                                #also if the parameter (the greeting thing) was not filled we can add a default value 
                                #by just adding a = '' we can do that to all parameters in the function
def hotel_waitress(greeting = 'Hello', name = 'Sir.'):
    return '{}, {}'.format(greeting, name)
print(hotel_waitress())
print(hotel_waitress('Good morning', 'Ma\'am.'))
print()

def student_info(*args, **kwargs): #now this might look confusing at first but lets just think that args are just
    print(args)                     #lets just say that args are the positional arguements that are in a tuple
    print(kwargs)                   #and kwargs are keyword values or extra info i guess in a dictionary

student_info('CompSci', 'Geography', name = 'Izaz', age = '15') #ALSO DO NOT FORGET IT IS NOT A RETURNING VALUE
                                                            #so use its own function name and not print()
print()
                                            #now u see that when i typed the student_info it was a huge long line and 
                                            #kind of messy, we can actually insert lists, tuples dictionaries and stuff
                                            #into the args and kwargs
classes = ['Compsci', 'Math']
info = {'name': 'Izaz', 'age':  15}
student_info(classes, info)             #now as u can see it aint up to our expectations, because vscode
                                        #thought both of the classes and info are the same args, we can separate them
                                        #and unpack them by adding the corresponding stars '*' from the args and kwargs
print()
student_info(*classes, **info) #boom

#alright onto the exercise a whole lot was learned
#Exercise
# Day 7 Challenge
# 🎮 RPG Character Creator

# This challenge uses almost everything from today's lesson.

# Requirements

# Create three functions.

# Function 1
# welcome()

# Print:

# ====================
#  RPG CHARACTER CREATOR
# ====================
# Function 2
# create_character(name, job="Warrior")

# It should return something like:

# Name: Izaz
# Class: Warrior

# Notice:

# job has a default value.
# Function 3
# show_inventory(*items)

# If the user enters:

# Sword
# Potion
# Shield

# Output:

# Inventory

# 1. Sword
# 2. Potion
# 3. Shield

# Use *args.

# Main Program

# Call the functions.

# Example:

# Enter name: Izaz
# Choose class (leave blank for Warrior): Mage

# Output:

# ====================
#  RPG CHARACTER CREATOR
# ====================

# Name: Izaz
# Class: Mage

# Inventory

# 1. Sword
# 2. Potion
# 3. Shield
# ⭐ Bonus

# Create:

# character_stats(**stats)

# Call it like:

# character_stats(
#     health=100,
#     mana=50,
#     level=3
# )

# Output:

# Character Stats

# Health: 100
# Mana: 50
# Level: 3

# Loop through kwargs.

# ⭐⭐ Final Boss

# Create one function that combines everything.

# Something like:

# create_profile(name, job, *items, **stats)

# so you can call it like:

# create_profile(
#     "Izaz",
#     "Mage",
#     "Sword",
#     "Potion",
#     "Shield",
#     health=100,
#     mana=50,
#     level=5
# )

# That will probably make your brain hurt for about 15 minutes, which is usually a sign you're learning rather than just typing. 😄
print()
def welcome():
    print('Greetings player.')

def create_character(name, job="Archer"):
    return '''Name: {}
Class: {}'''.format(name, job)
def show_inventory(*args):
    for index, item in enumerate(inv, start=1):
        print(f'{index}. {item}')
def input_inven():
    inputed_inv = input('Please enter 3 inventory items: ')
    inv.append(inputed_inv)
inv = []


welcome()
print()
input_inven()
input_inven()
input_inven()

print('''====================
 RPG CHARACTER CREATOR
====================''')
print()
print(create_character('Izaz', 'Spy'))
print()
print('Inventory')
print()
show_inventory(*inv)

#yeah so day 7 complete in a car going to malanggg gaddamn i just wanna be consistent
#please be worth it.
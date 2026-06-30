#LISTS TUPLES & SETS

food = ['Burger', 'Pizza', 'Fries', 'Rice'] #This is a list made with those square brackets.
                                            # you can add stuff to the lists without changing the list itself by using .append()
food.append('Chicken') #This will add chicken to the end of the list

food.insert(2, ('Egg')) # to add something into the list in a specific place in the list we can use .insert(index, 'value')

food2 = ['Meat', 'Croissant'] #Now we can extend a different list to the main list by using .extend()
food.extend(food2)

                            #to remove a specific item from a list we can use .remove('item')
food.remove('Fries')
                            #but to remove an item from the end of a list we can use .pop()
food.pop() 
                            #to reverse the list entirely we can use .reverse()
food.reverse()
                            #to sort out a list in an alphabetical order we can use .sort()
food.sort()                 #this can also be sorted('value'), instead of just .sort()
                            #.sort() could also be used in number lists to make them in an ascending order
num = [2,5,6,3]
num.sort()
                            #but .sort() also could be used in an descending order or a reverse way (not using .reverse)
                            #by using .sort(reverse=true)
num.sort(reverse=True)
food.sort(reverse=True)
                            #Don't forget that we can also just make them into variables so we dont have to change the whole list
                            #entirely but only some methods can, ex. popped = food.pop() will return the value that is popped
sortednum = sorted(num)
                            #min max sum is also a thing in python same with the ones in excel bla bla bla

                            #We can check if values are in the list by using this
print('Burger' in food)     #its a boolean basically (Don't forget everything is capital sensitive)
print(food) 
print(sortednum)
print()

#Looping Values
for item in food:
    print(item)             #This code basically repeats the code till the whole thing is done and puts every "item"
print()                     #in a new line BY DEFAULT.

                            #Now enumerate(value) enumerate is basically another looping value where now includes numbers BESIDE
                            #the value , depends on what were looking for ex. the index in every item of the list
for index, food2 in enumerate(food2):
    print(index, food2)
print()
                            #now because index starts at 0 we can actually set the starting number to anything by using
                            #enumerate(food, start=1)
for index, food in enumerate(food, start=1):
    print(index, food)
print()
                            #so to convert the list into a string, we can use 'any'.join('value')
friends = ['Rasyid', 'Keyvan', 'Dhika', 'Hammam']
foodstr = ', '.join(friends)
print(foodstr)
                            #we can also remove the joined stuff in the list (foodstr) by using .split('value')
newfriends = foodstr.split(', ')
print(newfriends)
print()

#Tuples
                            #Tuples are basically similar to lists but with 1 major difference which is that it cannot be
                            #modified, lists are mutable(changable) and tuples are not (immutable)
l1 = ['poop', 'piss', 'fart']
l2 = l1

print(l1)
print(l2)
print()
l1[0] = 'shit'

print(l1)
print(l2)                   #This is a normal list which is mutable and changable(modified)

t1 = ('mom', 'dad', 'siblings')
t2 = t1

print(t1)
print(t2)
print()
# t1[0] = 'mother'
# print(t1)
# print(t2)                 #now if this were to be runned it would be an error because its a tuple(immutable) and it is
                            #not to be changed, the only difference being is that lists use square brackets and tuples uses
                            #parentheseses '()' 
#Sets
                            #sets are basically lists but using braces {} and when executed they go unordered, they basically
                            #ignore every duplicate value IN the set
main_family = {'mama', 'papa', 'sister', 'brother', 'me'}
diff_family = {'mama', 'papa', 'me', 'uncle', 'aunt'}

print(main_family.intersection(diff_family)) #intersection() is basically modus, the ones that appear the most
                                            # or you could say the value that appears at 2 different lists
print(main_family.difference(diff_family))#difference() is basically the values that doesnt appear at the intersection
                                        # of 2 different lists, or u could say the values that's on its own.
print(main_family.union(diff_family))#basically combines both of the lists into one in an UNORDERED ORDER because duh its a set
                                    #not a list or a tuple.
print()

#empty lists
emp_list = []
emp_list = list() #both are usable

#empty tuples
emp_tuple = ()
emp_tuple = tuple() #both are usble

#empty sets
emp_set = {} #THIS IS NOT USABLE this is a dictionary not a set
emp_set = set() #this is usable :)

#Exercise
# Requirements

# Ask the user:

# Username
# 5 favorite games

# Store them in a list.

# Print:

# ====================
#  STEAM LIBRARY
# ====================

# Username: blackifiedbro

# Games:
# 1. Roblox
# 2. Deepwoken
# 3. Minecraft
# 4. Terraria
# 5. Elden Ring

# username = input("What is your username: ")
# print()
# game1 = input("What is your 1st favorite game: ")
# game2 = input("What is your 2nd favorite game: ")
# game3 = input("What is your 3rd favorite game: ")
# game4 = input("What is your 4th favorite game: ")
# game5 = input("What is your 5th favorite game: ")

# fav_games = [game1, game2, game3, game4, game5]

# print('''====================
#  STEAM LIBRARY
# ====================''')
# print()
# print(f'Username: {username}')
# print()
# print('Favorite games:')
# for index, games in enumerate(fav_games, start=1):
#     print(f"{index}. {games}")





#Extra Exercise
# Challenge: RPG Character Creator
# Goal

# Create a program that asks the user to create 5 characters.

# Use a loop.

# Output Example
# How many characters would you like to create? 5

# Character #1: Knight
# Character #2: Archer
# Character #3: Mage
# Character #4: Rogue
# Character #5: Healer

# Store them in a list.

# After that print:

# ====================
# YOUR PARTY
# ====================

# 1. Knight
# 2. Archer
# 3. Mage
# 4. Rogue
# 5. Healer

# Use enumerate().

# ⭐ Bonus 1

# Print:

# Total characters: 5

# using len().

# ⭐⭐ Bonus 2

# Print:

# First character:
# Knight

# Last character:
# Healer

# using indexing.

# ⭐⭐⭐ Bonus 3

# Ask:

# Who is your favorite character?

# If it's in the list:

# Knight is in your party!

# Otherwise:

# That character isn't in your party.

# (Hint: the in keyword.)

# 🔥 Final Boss

# After the list is finished...

# Print everything in uppercase.

# Example:

# 1. KNIGHT
# 2. ARCHER
# 3. MAGE
# 4. ROGUE
# 5. HEALER

totalchar = int(input("How much characters would you like to make? "))
characters = []
print()
for i in range(totalchar):
    character = input(f"Character {i + 1}: ")
    characters.append(character)
print()
print('''====================
YOUR PARTY
====================''')
print()

for index, character in enumerate(characters, start=1):
    print(f"{index}. {character.upper()}")
print()
print(f"Total Characters: {totalchar}")
print('First Character: ')
print(characters[0].upper())
print('Last Character: ')
print(characters[-1].upper())
print()
favchar = input('Who is your favorite character: ')
if favchar in characters:
    print(f'{favchar} is in your party!')
else:
    print('Your favorite character is not in your party.')



#honestly fun exercises but i spent like 3h on the LAST DEBUGGING ON THE STUPID EXERCISE
#but lowkey it was fun           fuh yeah day 3 BABYYYYYYYYYYYYYYYYYYYYYYYYYYYY
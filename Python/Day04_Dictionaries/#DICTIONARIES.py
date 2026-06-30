#DICTIONARIES

me = {'name': 'Izaz', 'age': 14, 'subjects': ['English', 'CompSci']} #the ones inside the braces are called keys (THIS ISNT A SET)

print(me) #just a normal print but we can also specify a certain key to just be printed
print(me['name']) #like this
                # but keys could be integers too not only strings
                # usually if we try to print a key that doesnt exist it would print out a key error, but theres also an alternate way to search for a key
                #by using .get('key')
print(me.get('dad'))# it would print out none instead of a key error, but we can change this "none" into anything else
print(me.get('dad', 'Dad is gone.')) # like this
print()
                                    #We can also add a key to a dictionary by doing it like this
me['mom_num'] = '08-123'
print(me.get('mom_num', 'wrong num')) # likee this, ALSO DO NOT FORGET THE '' FOR INSERTING KEYS i always forget.
                                    #Also we can overwrite/update keys by doing the same thing as inserting a key but now putting an already existing key name.
me['name'] = 'Akbar'
print (me)              #like this :)
                                    #its also possible to update more than 1 keys at once, by using .update({'key' = '', })
me.update({'name': 'Juliet', 'age': '18', 'mom_num': '+62 813'})
print(me)                            #like thissss :D
print()
                                    # Now to delete a certain key and its value we can use del NOT .del so its infront.
del me['mom_num']                   #using brackets btw not parentheses
print(me) 
                                    #also similar to lists dictionary keys can also be popped (deleted) and returned to its variable like in lists
                                    #but i just didnt mention it
psubject = me.pop('subjects')
print(psubject)
print(me)                           #like this. (man i keep forgetting to use parentheses or brackets smh)
                                    #again similar to lists, strings (len()) also works here, it counts how many keys are IN the dictionary
print()
print(len(me))                      #its very few (2) because i deleted/removed most of the keys now its only 'name' and 'age'
                                    #instead of counting how many keys theres also a way to see all the keys and values using their corresponding names
print(me.keys())
print(me.values()) 
                                    #theres also a way to see both keys and values (their pairs) by using .items
print(me.items())
print()
                                    # now again similar to lists we can also use loops, we can loop through keys, values, and pairs
for key in me:
    print(key)
print()
for value in me.values():
    print(value)
print()
for pairs in me.items():
    print(pairs)
print()                             #like these!

#Exercise
# Challenge: Player Database

# You're making a tiny database for an RPG game.

# Part 1

# Create an empty dictionary.

# player = {}

# Ask the user for:

# Username
# Level
# Health
# Favorite Weapon

# Store all of them inside the dictionary.

player = {}

username = input('What is your username: ')
player['Username'] = f'{username}'
level = int(input('What is your level: '))
player['Level'] = f'{level}'
health = int(input('How much health do you have: '))
player['Health'] = {f'{health}'}
f_weapon = input('What is your favorite weapon: ')
player['Favorite Weapon'] = f'{f_weapon}'

print(f'{username}\'s stats:')
for pairs in player.items():
    print(pairs)

#needs improvement in the future.







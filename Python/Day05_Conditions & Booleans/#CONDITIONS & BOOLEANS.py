#CONDITIONS & BOOLEANS 
#cmon you already know this mostly, if else elif, we use comparisons such as ==, !=, <=, >=.
me = 'Izaz'
if me == 'Izaz':
    print('I\'m Izaz')
else: print('I\'m not Izaz')

#now using and, or, not its pretty self explanatory
dad = 'dead'
alive = False
if dad == 'dead' and alive:
    print('DAD IS HERE!')
else: print('Dad isn\'t here')


#now using "is" basically checks if an id of an object is the same likeee this
print()
a = ['a, b, c']
b = ['a, b, c'] #now they HAVE the same memory/values but theyre not the same (id) different lists basically

print(a == b) #true
print(a is b) #false
                #now we can check ids on stuff by using id()
print(id(a))
print(id(b))

a = ['a, b, c'] 
b = a           # < but we can also just do this if we want to make the same list i guess.
print()
print(a == b)
print(a is b)
print(id(a))
print(id(b))

#False values
#False
#None
#Zero of any numeric type
#empty sequences () '' []
#empty mappings {}

cat = None
print()
if cat == True:
    print('Cat is here')
else: print('Cat ain\'t here') 
                                #BASICALLY if any value is filled like with something its true, but if theres nothing its false bla bla bla
 
#VERY simple and short notes mainly cause i already understand 95% of the stuff but yeah exercise time

#Exercise
# Challenge: Login System

# This uses almost everything from your notes.

# Goal

# Create a tiny login system.

# Step 1

# Store these credentials:

# correct_username = "blackifiedbro"
# correct_password = "python123"

# Ask the user to enter both.

# Step 2

# Use conditionals.

# If both are correct:

# Login successful!

# Else:

# Incorrect username or password.
# ⭐ Bonus 1

# If only the username is wrong:

# Username not found.

# If only the password is wrong:

# Incorrect password.

# Otherwise:

# Login successful!

# (Hint: if, elif, else)

# ⭐⭐ Bonus 2

# Ask:

# Are you an admin? (yes/no)

# If they're logged in and they're an admin:

# Welcome, Administrator.

# Otherwise:

# Welcome, User.

# (Hint: and)

# ⭐⭐⭐ Bonus 3

# Create two variables:

# inventory1 = ["Sword", "Potion"]
# inventory2 = ["Sword", "Potion"]

# Print:

# print(inventory1 == inventory2)
# print(inventory1 is inventory2)

# Then do:

# inventory2 = inventory1

# Print them again.

# Finally, write one comment in your own words explaining why the results changed.

# No copying. Explain it like you're teaching yourself.

# ⭐⭐⭐⭐ Final Boss

# Create this:

# inventory = []

# Check:

# if inventory:

# Print:

# Inventory has items.

# Otherwise:

# Inventory is empty.

# Then add:

# inventory.append("Sword")

# Run it again.

# See what changes.
print()


#Login
username = input('What is your username: ')
password = input('What is your password: ')
admin = input('Are you an admin? ')

print('''===============
LOGIN
==============''')
print()
enter_username = input('Username: ')
enter_password = input('Password: ')
if username == enter_username and password == enter_password and admin == 'Yes':
    print()
    print('Welcome Admin')
elif username == enter_username and password == enter_password and admin == 'No':
    print()
    print('Welcome User')
elif username != enter_username and password == enter_password:
    print()
    print('Invalid username')
elif username == enter_username and password != enter_password:
    print()
    print('Invalid password')
elif username != enter_username and password != enter_password:
    print()
    print('Invalid credentials')
else: print('Error please try again')
print()

#Bonus 3
family1 = ['Mom', 'Dad']
family2 = ['Mom', 'Dad']

print(family1 == family2)
print(family1 is family2)
print()

family2.pop()
family2.pop()
family2 = family1
print(family1 == family2)
print(family1 is family2) #It changed values from true and false to true and true because at the 1st print == checks for equal values NOT id's
                            #so it returned as true because family1 and 2 has same values as 'Mom', 'Dad' but for the 2nd print 'is' checks for THE SAME IDS
                            # they have same values but are 2 different variables making it a separate and different ids so it results as false
                            #those 2 == and 'is' explains why now when i removed every value from family2 and made it family2 = family1
                            # both prints returns as true because family2 is made identical as family1 because family2 got assigned as family1
                            #hopefully that makes sense
print()
#Last Bonus
inv = []
if inv:
    print('It has items in it')
else: print('It\'s empty')

inv.append('Axe')
if inv:
    print('It has items in it')
else: print('It\'s empty')
                            #now for this one, at the first time i did the if statements it returned as false and inv was empty because empty brackets  
                            # are considered as a false value so it returned as false
                            #as when i appended a new value to the list ('Axe') it returned as true and has items in it
                            # thats because when i appended the axe the list became filled and not empty anymore and now is refered as True.
                            #hopefully that makes sense its in my own words

#ALLRIGHT this only took me like an hour, this is day 5 and i did the challenges pretty fast compared to those last 4 days
#shows how much i learned, which makes me proud and gives me more motivation to be consistent on this python project,
#hopefully i don't miss a day andd for today ill rate it a 9.2/10 pretty noice 
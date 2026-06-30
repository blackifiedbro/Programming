#STRINGS

#EXPLANATIONS.
m = "Hello World" # this is a string

        #you can use single or double quotes to create a string

m = 'Hello World' # this is also a string

# m = 'bobby's world'  
# this will cause an error because of the single quote in "bobby's" so add a backslash before the single quote to escape it
mb = 'bobby\'s world' # this will work

# use triple quotes for multi-line strings (''' or """)

mm = '''mother likes cooking
and father likes fishing'''

#LENGTHS, INDEXING, SLICING.

#Length of a string can be found using the len() function
print(len(m)) # this will print 11
print(len(mb)) # this will print 13
print(len(mm)) # this will print 45

#Indexing allows you to access individual characters in a string using their position (index). The index starts at 0 for the first character.
print(m[0]) # this will print 'H'
print(mb[0]) # this will print 'b'
print(mm[0]) # this will print 'm'

#Slicing allows you to access a range of characters in a string using their positions.
print(m[0:5]) # this will print 'Hello'
print(mb[0:5]) # this will print 'bobby'
print(mm[21:]) # this will print 'mother'
print(m[6:11]) # this will print 'World'

#STRING METHODS.

#Converting to Uppercase and Lowercase
print(m.upper()) # this will print 'HELLO WORLD'
print(m.lower()) # this will print 'hello world'

#Searching & Counting
print(m.find('World')) # this will print 6 (basically the index of the first character of the substring 'World')
print(m.count('o')) # this will print 2 (the number of occurrences of 'o')

#Replacing
print(m.replace('World', 'Universe')) # this will print 'Hello Universe'

#STRING CONCATENATION AND FORMATTING.

#Concatenation is the process of joining two or more strings together using the + operator.
greeting = "Hello"
Name = "Rasyid"

Goodbye = greeting + ", " + Name + ". See you next time!" # this will create a new string 'Hello Rasyid. See you next time!'
print(Goodbye) # this will print 'Hello Rasyid. See you next time!'

#It's very long so to make it simpler, we can use f-strings to format strings in a more readable way.
Goodbye_f = f"{greeting}, {Name}. See you next time!"
print(Goodbye_f) # this will print 'Hello Rasyid. See you next time!'

#INSPECTING STRINGS.

#dir(variable) function can be used to inspect the methods and attributes of a string variable.
# print(dir(m))     this will print a list of all the methods and attributes of the string

#help(type) function can be used to get help on the string type and its methods.
# print(help(str))     this will print the help documentation for the string type

#help(method) function can be used to get help on a specific method of a string variable.
# print(help(m.upper))     this will print the help documentation for the upper() method of the string variable m



#the code is greyed out so it doesnt take up the whole space yk yk also first time in a while
#ive used python and its been a while since ive used it so i might have forgotten some stuff but i think this is a good refresher for me and for anyone else who might be reading this.
#and im very suprised its smart on filling alot of the stuff
#so this is day one! yippee!!!
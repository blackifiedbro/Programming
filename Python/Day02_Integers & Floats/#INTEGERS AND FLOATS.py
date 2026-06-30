#INTEGERS AND FLOATS

n = 10
print(n) # This will print as an integer (int)
n = 3.14
print(n) # This will print as a float 

#Int's are whole numbers, while floats are decimal numbers.

#ARITHMETIC OPERATORS
print(5 + 3)  # Addition
print(5 - 3)  # Subtraction
print(5 * 3)  # Multiplication
print(5 / 3)  # Division
print(5 // 3) # Floor Division (Whole number without decimals/remainders)
print(2 ** 3) # Exponentiation (Pangkat)
print(5 % 3)  # Modulus (Sisa bagi)
print()

#Incrementing & Decrementing Numbers
n = 10
print(n)
n += 1  # Increment by 1
print(n)
n -= 1  # Decrement by 1
print(n)
#You can do this with every arithmetic operator, for example:
n *= 2  # Multiply by 2
print(n)
n /= 2  # Divide by 2
print(n)
print()

#Extra abs and round functions
n = -10
print(abs(n)) # Absolute value
n = 3.14159
print(round(n)) # Round to nearest whole number
print(round(n, 2)) # Round to 2 decimal places
print()

#Comparison Operators (Boolean is a true or false value)
n1 = 14
n2= 8
print(n1 > n2)  # Greater than
print(n1 < n2)  # Less than
print(n1 == n2) # Equal to
print(n1 != n2) # Not equal to
print(n1 >= n2) # Greater than or equal to (Lebih besar dari atau sama dengan)
print(n1 <= n2) # Less than or equal to (Kurang dari atau sama dengan)
print()

#Casting Numbers
nc = '10'
nf = '100'

#Casting is converting one data type to another data type, if we print
#nc + nf, it will print 10100 because they are both strings. To convert them to integers, we can use the int() function.
print(int(nc) + int(nf)) # This will print 110 because they are both int's now.
#we can also convert them to floats using the float() function.
print(float(nc) + float(nf)) # This will print 110.0 because they are both floats now.


#Exercise
#Challenge: Pizza Bill Calculator

#Create a program that asks the user:

#Customer name
#Price of Pizza
#Price of Drink
#Price of Dessert

#Then calculate:

#Total price
#Add a 10% service charge
#Display the final amount

print()
print()

print('''====================
 PIZZA RECEIPT
====================''')
print()
customer = input('Customer Name: ')
print()
pizza = float(input('''Price of Pizza: $'''))
drink = float(input('''Price of Drink: $'''))
dessert = float(input('''Price of Dessert: $'''))
print()
subtotal = pizza + drink + dessert
total = subtotal + (subtotal * 0.1) # Add 10% service charge
service = subtotal * 0.1
print(f'''Subtotal: ${subtotal:.2f}
Service Charge (10%): ${service:.2f}''')
print()
print(f"Total: ${total:.2f}")
pay = input('Enter amount to pay: ')
change = float(pay) - total
print(f"Change: ${change:.2f}")
print()
print(f"thanks for your order {customer}!".upper())

#day 2 and im proud of my progress even though chatgpt said i couldve had more improvements but overall W

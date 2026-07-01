#notes
#LOOPS & ITERATIONS

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num) #normal for Loop
                #now using break statement
print()
for num in nums:
    if num == 3:
        print("Found 3!")
        break
    print(num) #breaks the loop when num is 3
                #now continue statement
print()
for num in nums:
    if num == 3:
        print("Found 3!")
        continue
    print(num) #when it finds 3 it doesnt stop like the break statement
                #it continues the code/loop and prints the rest of the numbers

                #now loops within loops
print()
for num in nums:
    for letter in 'abc':
        print(num, letter) #prints all the numbers with all the letters
print()
                            #now using range function
for i in range(10):
    print(i) #prints numbers from 0 to 9
            #but an alternate way is to use range(1, 10) it prints 1-9
print()
for i in range(1, 10):
    print(i) #prints numbers from 1 to 9
            #if we want number starting from 1 to 10 we can use range(1, 11)
print()
for i in range(1, 11):
    print(i) #prints numbers from 1 to 10
print()
                #now while loops
                #basically it runs the loops till a condition is met
nums = 0
while nums <= 2:
    print(nums)
    nums += 1 #prints numbers from 0 to 2

print()
number = 0
                #now using while loop with break statement
while number < 10:
    if number == 5:
        print("Found 5!")
        break
    print(number)
    number += 1 #prints numbers from 0 to 10 but breaks when it finds 5
print()
x = 0
                #now infinite loops that runs forever until a condition is met
while True:
    if x == 7:
        print("Found 7!")
        break
    print(x)
    x += 1 #prints numbers from 0 to 10 but breaks when it finds 7

                #NOW DISCLAMER IF YOU WERE TO RUN A WHILE TRUE CODE,
                #IT WILL RUN FOREVER AND U CAN STOP IT BY PRESSING CTRL + C

#ok thats just all for the vid ig, so i only learned like 40% more of loops
#with the while loops and while true thing, noww onto the exercise
#also the vscode assistant is back so most of the time itll do most of the debugging
#will save alot of time but makes me kind of feel lazy, but ill still try to learn

#Exercise
#ill put the exercise at the end because if i put it in the start the assistant
#will just do it for me and i wont learn anything, so ill just put it at the end


while True:
    name = input('Enter your warriors\' name: ')
    enemies_entered = int(input('How many enemies would you like to fight? '))
    print()
    print('''====================
 TRAINING ARENA
====================''')
    for enemyentered in range(1, enemies_entered + 1):
        if enemyentered == 3:
            print('Enemy 3 has appeared!')
            print('Enemy 3 ran away!')
            continue
        elif enemyentered  == 7:
            print('Boss appeared!')
            print('You escaped!')
            break
        print(f'Enemy {enemyentered} has appeared!')
        print(f'Enemy {enemyentered} defeated!')
    print()
    fight = input('Would you like to train again? (yes/no) ')
    if fight.lower() == 'yes':
        continue
    if fight.lower() == 'no':
        print()
        print(f'Thanks for training {name}!')
        break
    
# Challenge: RPG Training Arena
# Goal

# Create a tiny training simulator.

# Step 1

# Ask the user:

# Enter your warrior's name:

# Then ask:

# How many enemies would you like to fight?
# Step 2

# Print

# ====================
#  TRAINING ARENA
# ====================
# Step 3

# Use a for loop with range().

# Example:

# If the user enters 5:

# Enemy 1 appeared!
# Enemy 2 appeared!
# Enemy 3 appeared!
# Enemy 4 appeared!
# Enemy 5 appeared!
# ⭐ Bonus 1 (continue)

# If the enemy number is 3:

# Print

# Enemy 3 ran away!

# Then use continue.

# So it should NOT print

# You defeated Enemy 3!
# ⭐⭐ Bonus 2 (break)

# When the enemy number reaches 7:

# Print

# A Boss appeared!
# You escaped!

# Then stop the loop using break.

# Even if the player wanted to fight 20 enemies.

# ⭐⭐⭐ Bonus 3 (while loop)

# After the battle:

# Ask:

# Train again? (yes/no)

# Keep asking until they type either:

# yes

# or

# no

# If they type:

# banana

# Print

# Invalid option.

# and ask again.

# (Hint: while True.)

# ⭐⭐⭐⭐ Final Boss

# Count how many enemies were actually defeated.

# Example:

# If the user fought:

# 1
# 2
# 3 (ran away)
# 4
# 5
# 6
# 7 (boss)

# Output:

# Training complete!

# Warrior: BlackifiedBro

# Enemies defeated: 5

# Notice:

# Enemy 3 doesn't count.
# Enemy 7 doesn't count because you escaped.


#summary i mean not bad but kind of bad too it took me to the next morning to actually make the challenge work.
#but overall nice
    
            

    

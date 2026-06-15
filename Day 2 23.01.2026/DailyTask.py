### 
# Task 1 level 8
# 
# We need a simple function that determines if a plural is needed or not. It should take a number, 
# and return true if a plural should be used with that number or false if not. 
# This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
# 
# You only need to worry about english grammar rules for this kata,
# where anything that isn't singular (one of something), it is plural (not one of something).
###


def plural(n):
    return False if n == 1 else True


### 
# Task 2 level 7
# 
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
###

def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

# print(validate_pin("123456"))


### 
# Task 3 level 8
# 
# In this game, the hero moves from left to right. The player rolls the die and moves 
# the number of spaces indicated by the die two times.
# Create a function for the terminal game that takes the current position 
# of the hero and the roll (1-6) and return the new position.
###

def move(position, roll):
    return position + (roll * 2)

# print(move(0, 4))


### 
# Task 4 level 7
# 
# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking the other and whoever kills the other first is victorious.
# Death is defined as having health <= 0.
# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0.
# You can mutate the Fighter objects.
# Your function also receives a third argument, a string, with the name of the fighter that attacks first.
###
from Fighter import Fighter

def declare_winner(fighter1, fighter2, first_attacker):
    
    is_first_fighter1 = fighter1.name == first_attacker
    if is_first_fighter1:
        attacker = fighter1
        defender = fighter2
    else:
        attacker = fighter2
        defender = fighter1
    
    while(True):
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0: return attacker.name
        attacker.health -= defender.damage_per_attack
        if attacker.health <= 0: return defender.name
       


Lew = Fighter("Lew", 10, 2)
Harry = Fighter("Harry", 5, 4)
Harald = Fighter("Harald", 20, 5)

print(declare_winner(Harald, Harry, "Harry"))
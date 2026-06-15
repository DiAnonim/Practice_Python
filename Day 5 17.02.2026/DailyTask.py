### 
# Task 1 level 6
# 
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown
###


def likes(names):
    if not names: 
        return "no one likes this"
    
    names_len = len(names)
    
    if names_len == 1:
        return f"{names[0]} likes this"
    
    if names_len == 2:
        return f"{names[0]} and {names[1]} like this"
    
    if names_len == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    
    if names_len >= 4:
        return f"{names[0]}, {names[1]} and {names_len - 2} others like this"


# print( likes([]) )
# print( likes(["Peter"]) )
# print( likes(["Jacob", "Alex"]) )
# print( likes(["Max", "John", "Mark"]) )
# print( likes(["Alex", "Jacob", "Mark", "Max", "jnvsold"]) )



### 
# Task 2 level 8
# 
# The geese are any strings in the following array, which is pre-populated in your solution:
#   ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:
#   ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array:
#   ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, 
# albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, 
# and some elements may be repeated.
###


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

# print( goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) )


### 
# Task 3 level 7
# 
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!
###


def square_digits(num):
    result = ""
    
    for n in str(num):
        result += str(int(n) ** 2)
    
    return int(result)


# print( square_digits(9119) )


### 
# Task 4 level 5
# 
# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.
###


def increment_string(string):
    if not string or string.isalpha():
        return string + "1"
    
    str_len = len(string)
    last_number = int(string[str_len - 1])
    
    if last_number < 9:
        return string[:str_len - 1] + str(last_number + 1)
    else:
        last_number = ""
        
        for n in string[::-1]:
            if n.isalpha(): break
            last_number += n
            
        str_cut = -len(last_number)
        new_number = int( last_number[::-1] ) + 1
        
        return string[:str_cut] + str(new_number)
    

print( increment_string("") )
print( increment_string("foo") )
print( increment_string("foobar001") )
print( increment_string("foobar1") )
print( increment_string("foobar00") )
print( increment_string("fo99obar99") )
print( increment_string("fo99obar899") )
print( increment_string("fo99obar0") )
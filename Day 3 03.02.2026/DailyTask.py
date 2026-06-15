### 
# Task 1 level 6
# 
# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value. 
# The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; 
# target will always be the sum of two different items from that array).
###


def two_sum(numbers, target):
    for first_idx, first_number in enumerate(numbers):
        for second_number in numbers[first_idx + 1:]:
            if first_number + second_number == target:
                second_idx = 0
                if first_number == second_number:
                    second_idx = numbers.index(second_number, first_idx + 1)
                    return (first_idx, second_idx)
                second_idx = numbers.index(second_number)
                return (first_idx, second_idx)


# print(two_sum([1, 2, 3], 4))
# print(two_sum([1234,5678,9012], 14690))
# print(two_sum([2, 2, 3], 4))


### 
# Task 2 level 8
# 
# Sentence Smash
# 
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
###


def smash(words):
    return " ".join(words)


# print(smash(['hello', 'world', 'this', 'is', 'great']))




### 
# Task 3 level 8
# 
# Americans are odd people: in their buildings, the first floor is actually the ground floor 
# and there is no 13th floor (due to superstition).
# Write a function that given a floor in the american system returns the floor in the european system.
# With the 1st floor being replaced by the ground floor and the 13th floor being removed, 
# the numbers move down to take their place. In case of above 13, they move down by two because there 
# are two omitted numbers below them.
# Basements (negatives) stay the same as the universal level.
###

def get_real_floor(n):
    if n > 0 and n < 14:
        return n - 1
    elif n > 13: 
        return n - 2
    return n
    

# print(get_real_floor(1))
# print(get_real_floor(5))
# print(get_real_floor(15))
# print(get_real_floor(1))


### 
# Task 4 level 8
# 
# Complete the function which converts hex number (given as a string) to a decimal number.
###


def hex_to_dec(s):
    return int(s, 16)

print(hex_to_dec("1"))
print(hex_to_dec("a"))
print(hex_to_dec("10"))
print(hex_to_dec("6a48f82d8e828ce82b82"))
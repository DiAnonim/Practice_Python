### 
# Task 1 level 7
# 
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
# [10, 343445353, 3453445, 3453545353453] should return 3453455.
###


def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    return min1 + min2

# print( sum_two_smallest_numbers( [5, 8, 12, 18, 22]) )

### 
# Task 2 level 8
# 
# Kata Task
# I have a cat and a dog.
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]
# 
# NOTES:
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that
###

def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    cntIf = 0
    
    if human_years >= 1:
        catYears += 15
        dogYears += 15
        
        cntIf += 1
        
    if human_years >= 2:
        catYears += 9
        dogYears += 9
        
        cntIf += 1
    
    catYears += 4 * (human_years - cntIf)
    dogYears += 5 * (human_years - cntIf)
    
    return [human_years, catYears, dogYears]


print( human_years_cat_years_dog_years(1) )
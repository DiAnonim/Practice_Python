'''
In mathematics, the factorial of a non-negative integer n, denoted by n!, 
is the product of all positive integers less than or equal to n. 
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. 
If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) 
or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) 
or ValueError (Python) or return -1 (C).

'''

def factorial(n):
    if n < 0 or n > 12: raise ValueError("The value of n must be in the range from 0 to 12.")
    
    if n == 0: return 1
    
    res = 1
    for i in range(1, n + 1):
        res *= i
        
    return res

# print( factorial(-1) )


'''
What if we need the length of the words separated by a space to be added at 
the end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]

Your task is to write a function that takes a String and returns an Array/list 
with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.

'''

def add_length(str_):
    list_strs = []
    
    for s in str_.split():
        list_strs.append(f"{s} {len(s)}")
        
    return list_strs
    
# print( add_length("apple ban") )
# print( add_length("you will win") )


'''
Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with
all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

'''

def flatten_and_sort(array):
    one_dim_arr = [i for sublist in array for i in sublist]
    
    return sorted(one_dim_arr)


print( flatten_and_sort( [ [3, 2, 1], [4, 6, 5], [], [9, 7, 8] ] ) )
### 
# Task 1 level 5
# 
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five()))    #  must return 35
# four(plus(nine()))      #  must return 13
# eight(minus(three()))   #  must return 5
# six(divided_by(two()))  #  must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))
###

def zero(value = None): 
    if not value: 
        return 0
    return result(0, value[0], value[1])
    
def one(value = None): 
    if not value: 
        return 1
    return result(1, value[0], value[1])
    
def two(value = None): 
    if not value: 
        return 2
    return result(2, value[0], value[1])
    
def three(value = None): 
    if not value: 
        return 3
    return result(3, value[0], value[1])
    
def four(value = None): 
    if not value: 
        return 4
    return result(4, value[0], value[1])
    
def five(value = None):
    if not value: 
        return 5
    return result(5, value[0], value[1])
    
def six(value = None): 
    if not value: 
        return 6
    return result(6, value[0], value[1])
    
def seven(value = None): 
    if not value: 
        return 7
    return result(7, value[0], value[1])
    
def eight(value = None): 
    if not value: 
        return 8
    return result(8, value[0], value[1])
    
def nine(value = None): 
    if not value: 
        return 9
    return result(9, value[0], value[1])



def plus(num2):
    return [num2, "+"]

def minus(num2): 
    return [num2, "-"]

def times(num2):
    return [num2, "*"]
    
def divided_by(num2):
    return [num2, "/"]

def result(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    if oper == "-":
        return num1 - num2
    if oper == "*":
        return num1 * num2
    if oper == "/":
        if num2 == 0: return "ERROR: You can't divide by zero."
        return int(num1 / num2)




# print( seven( times( five() ) ) ) #  must return 35
# print( four( plus( nine() ) ) )      #  must return 13
# print( eight( minus( three() ) ) )   #  must return 5
# print( six( divided_by( two() ) ) )  #  must return 3
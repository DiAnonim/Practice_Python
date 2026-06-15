### 
# Task 1 level 8
# 
# Write a function that returns a string in which 
# firstname is swapped with last name.
###

### Task 1
# def name_shuffler(str_):
#     str_list = str_.split(" ")
#     str_ = f"{str(str_list[1])} {str(str_list[0])}"
#     return str_
    
# print(name_shuffler("john McClane"))




### 
# task 2 level 8
# 
# Write a function which takes a number and 
# returns the corresponding ASCII char for that value.
###

### Task2
# def get_char(c):
#   return chr(c)

# print(get_char(65))



### 
# task 3 level 7
# 
# Given a string str, reverse it and omit all non-alphabetic characters.
###

### Taks 3
# def reverse_letter(st):
#   return "".join([char for char in st if char.isalpha()])[::-1]
  
  
# print(reverse_letter("ultr53o?n"))


### 
# task 4 level 7
# 
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
###

### Taks 4
# def replace_exclamation(st):
#   result = ""
  
#   for char in st:
    
#     if char in "aeiouAEIOU":
#       result += "!"
      
#     else: result += char
    
#   return result

# print(replace_exclamation("ABCDE"))



### 
# task 5 level 6
# 
# You will be given a number and you will need to return it as a string in Expanded Form
###

### Task 5
def expanded_form(num):
  str_num = str(num)
  max_number_len = len(str_num)
  result = ""
  
  for i, n in enumerate(str_num):
    if n != "0": 
      cnt_zero = max_number_len - (i + 1)
      result += f"{n}{"0" * cnt_zero} + "
        
  return result[:-3]
  
  
print(expanded_form(12))

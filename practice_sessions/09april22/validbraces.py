"""
Valid braces: https://www.codewars.com/kata/5277c8a221e209d3f6000b56

Instruction: 
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
"""

open_list = ["[","{","("]
closing_list = ["]","}",")"]

def valid_braces(string):
    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in closing_list:
            pos = closing_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


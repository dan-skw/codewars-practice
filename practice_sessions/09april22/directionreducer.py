"""
Directions reduction: https://www.codewars.com/kata/550f22f4d758534c1100025a

Instruction: 
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).
"""

def dirReduc(arr):
    
    reduced_arr= []
    dirdic = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    
    for direction in arr: 
        if reduced_arr and dirdic[direction] == reduced_arr[-1]:
            reduced_arr.pop()
        else:
            reduced_arr.append(direction)
    
    return reduced_arr
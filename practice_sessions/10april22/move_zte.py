"""
Moving zeros to the end: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros(array):
    for i in array:
        if i == 0:
            array.append(array.pop(array.index(i)))
    return array
"""
Create phone number: https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
"""

def create_phone_number(n):
    slist = list(map(str, n))
    return (f'({"".join(slist[0:3])}) {"".join(slist[3:6])}-{"".join(slist[6:10])}')
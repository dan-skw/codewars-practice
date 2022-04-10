"""
Highest Scoring Word: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
You need to return the highest scoring word as a string.
all me so im kinda proud of it
"""


def high(x):
    l_x = x.split(" ")
    s_l = []
    s_score = 0
    for word in l_x:
        for letter in word:
            s_score += ord(letter) - 96
        s_l.append(s_score)
        s_score = 0 
    return (l_x[s_l.index(max(s_l))])
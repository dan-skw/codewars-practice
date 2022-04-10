"""

Stop gninnipS My sdroW!: https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
"""

def spin_words(sentence):
    n_sen = []
    s_list = sentence.split()
    for word in s_list:
        if len(word) < 5:
            n_sen.append(word)
        else:
            n_sen.append(word[::-1])
    return " ".join(n_sen)
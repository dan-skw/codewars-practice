"""
Simple pig latin: https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""


def pig_it(text):
    sen_l = text.split()
    mod_sl = []
    mod_strin = ""
    for word in sen_l:
        if word.isalpha():
            mod_strin = word[1:]+word[0] + "ay"
            mod_sl.append(mod_strin)
        else:
            mod_sl.append(word)
    return " ".join(mod_sl)
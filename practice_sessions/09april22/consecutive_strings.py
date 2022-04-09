"""
Consecutive strings: https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

Instruction: 
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
"""

def longest_consec(strarr, k):
    final_conc_string = ""

    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr) - k + 1):
            conc_string = ''.join(strarr[i:i+k])
            if len(conc_string) > len(final_conc_string):
                final_conc_string = conc_string

    return final_conc_string
        
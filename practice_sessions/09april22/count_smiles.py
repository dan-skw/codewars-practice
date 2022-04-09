"""
Count the smiley faces!: https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

+ clever solution:
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

"""

def count_smileys(arr):
    
    if len(arr) == 0:   
        return 0

    smile_counter = 0
    for x in arr:
        if len(x) == 3:
            if (x[-1] == ")" or x[-1] == "D") and (x[0] ==":" or x[0] == ";") and (x[1] == "-" or x[1] == "~"):
                smile_counter += 1 
        elif len(x) == 2:
            if (x[-1] == ")" or x[-1] == "D") and (x[0] ==":" or x[0] == ";"):
                smile_counter += 1
        else:
            continue
    return smile_counter
    #smiles = [x for x in arr if (x[-1] == ")" or x[-1] == "D") and (x[0] ==":" or x[0] == ";") and (x[1] == "-" or x[1] == "~")]
    #return len(smiles)



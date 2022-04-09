"""
Find the unique number: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

There is an array with some numbers. All numbers are equal except for one. Try to find it!
"""

def find_uniq(arr):       
    first_num = arr[0]
    last_num = arr[-1]
    arr2set = set(arr)
    if first_num == last_num:
        for uvalue in arr2set:
            if uvalue == first_num:
                continue
            else:
                return uvalue
    elif first_num != arr[1]:
        return first_num
    else:
        return last_num


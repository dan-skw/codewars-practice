"""
Maximum subarray sum: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/python

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""

def max_sequence(arr):
    e_list = []
    for i in range(len(arr)+1):
        for j in range(i, len(arr)+1):
            e_list.append(sum(arr[i:j]))
    return max(e_list)
    

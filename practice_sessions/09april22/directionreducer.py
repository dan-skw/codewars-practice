def dirReduc(arr):
    
    reduced_arr= []
    dirdic = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    
    for direction in arr: 
        if reduced_arr and dirdic[direction] == reduced_arr[-1]:
            reduced_arr.pop()
        else:
            reduced_arr.append(direction)
    
    return reduced_arr
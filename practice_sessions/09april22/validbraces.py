open_list = ["[","{","("]
closing_list = ["]","}",")"]

def valid_braces(string):
    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in closing_list:
            pos = closing_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


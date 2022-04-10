def permutations(string):
    all_p = set([string])
    if len(string) <=1:
        return list(string)
    elif len(string) == 2:
        all_p.add(string[1] + string[0])
    return list(all_p)

print(permutations("ab"))
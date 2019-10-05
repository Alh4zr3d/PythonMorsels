from itertools import groupby

def compact(data):
    return(i for i,_ in groupby(data))
#    cmpcted = [i for i,_ in groupby(data)]
#    return iter(cmpcted)

# data = [1, 1, 2, 2, 3, 2]
# groups = []
# uniquekeys = []
# data = sorted(data)
# for k, g in groupby(data):
#    groups.append(list(g))      # Store group iterator as a list
#    uniquekeys.append(k)

# print(groups)
# print(uniquekeys)

# cmpcted = [i for i,_ in groupby(data)]
# print(cmpcted)
# print(iter(cmpcted))

def tail(seq,num):
    lst = list(seq)
    if num <= 0:
        result = []
    else:
        result = lst[-num:]
    return result

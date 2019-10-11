def tail(seq,num):
    result = []
    if num <= 0:
        return result
    elif num == 1:
        for n in seq:
            result = [n]
    else:
        for n in seq:
            result = [*result[-(num-1):],n]
    return result

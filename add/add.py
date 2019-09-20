def add(*args):
    test1 = len(args[0])
    for lst in args:
        if len(lst) != test1:
            raise ValueError("Given matrices are not the same size.")
        test2 = len(lst[0])
        for item in lst:
            if len(item) != test2:
                raise ValueError("Given matrices are not the same size.")
    result = []
    for items in zip(*args):
        added = []
        for set in zip(*items):
            added.append(sum(set))
        result.append(added)
    return result

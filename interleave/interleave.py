def interleave(lst1,lst2):
    for x in zip(lst1,lst2):
        for y in x:
            yield y

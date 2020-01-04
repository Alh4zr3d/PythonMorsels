from collections.abc import Iterable

def deep_add(iterable,start=0):
    result = start
    for item in iterable:
        if isinstance(item,Iterable):  # and not isinstance(item,(str,bytes)):
            result = deep_add(item,start=result)
        else:
            result += item
    return result

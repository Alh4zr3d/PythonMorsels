import re

def count_words(str):
    result = {}
    words = re.findall(r'\w+',str)
    for word in words:
        if word.lower() not in result.keys():
            result[word] = 1
        else:
            result[word] += 1
    return result
            

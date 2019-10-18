def count_words(str):
    result = {}
    wordchars = "abcdefghijklmnopqrstuvwxyz'"
    words = str.split()
    for word in words:
        word = word.lower()
        if word[0] not in wordchars:
            word = word[1:]
        if word[-1] not in wordchars:
            word = word[0:-1]
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] += 1
    return result
            

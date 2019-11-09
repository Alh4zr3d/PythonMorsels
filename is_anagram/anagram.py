import string
from unicodedata import normalize

def is_anagram(str1,str2):
    s1 = normalize('NFKD', str1).encode('ascii','ignore').decode()
    s2 = normalize('NFKD', str2).encode('ascii','ignore').decode()
    s1 = s1.translate(str.maketrans('', '', string.punctuation))
    s2 = s2.translate(str.maketrans('', '', string.punctuation))
    return sorted(s1.lower().replace(" ","")) == sorted(s2.lower().replace(" ",""))

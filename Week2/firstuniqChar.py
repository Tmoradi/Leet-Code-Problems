from collections import Counter
def firstUniqChar(s):
    counter_char = Counter(s)
    # print(counter_char)
    for key in counter_char.keys():
        if counter_char[key] == 1:
            return s.index(key)
    return -1
   

print(firstUniqChar('loveleetcode'))
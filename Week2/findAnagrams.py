from collections import Counter

def findAnagram(s,p):
    found = []
    
    have = Counter(s)
    want = Counter(p)

    for i in range(1,len(s)-len(p)+1):
        have[s[i-1]] -=1
        have[s[i+len(p)-1]] += 1
        if have[s[i-1]] == 0:
            del have[s[i-1]]
        if have == want:
            found.append(i)
    return found 

print(findAnagram('abab','ab'))


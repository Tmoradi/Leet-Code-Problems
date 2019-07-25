from collections import defaultdict
def isIsomorphic(s,t):
    s_2_t = defaultdict(str)
    t_2_s = defaultdict(str)
    for char1,char2 in zip(s,t):
        if char1 not in s_2_t and char2 not in t_2_s:
            s_2_t[char1] = char2
            s_2_t[char2] = char1
        elif s_2_t[char1] != char2 and t_2_s[char2] != char1:
            return False 
        
    return True

print(isIsomorphic('egg','add'))
print(isIsomorphic('foo','bar'))
print(isIsomorphic('paper','title'))
print(isIsomorphic('ab','aa'))

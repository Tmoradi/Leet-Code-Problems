from collections import defaultdict 

def wordPattern(pattern,string):
    # we can get a set of pattern and str
    
    str_ = string.split()
    if len(str_) != len(pattern):
        return False 
        
    pattern2str_ = {}
    str2pattern_ = {}

    for char,word in zip(pattern,str_):
        if (char in pattern2str_ and pattern2str_[char] != word) or (word in str2pattern_ and str2pattern_[word] !=char):
            return False
        else:
            pattern2str_[char] = word
            str2pattern_[word] = char
    return True 

print(wordPattern('abba','dog cat cat dog'))
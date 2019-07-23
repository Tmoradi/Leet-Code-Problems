def detectCapitalUse(self, word: str):
    #
    if (word == word.upper() or word == word.lower()):  
        return True 
    elif (word[0] == word.upper()[0] and word[1:] == word.lower()[1:]): 
        return True
    else:
        return False 
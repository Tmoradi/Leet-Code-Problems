def numJewelsInStones(J,S):
    # defining our dict to keep track of jewels we have 
    d = {jewel: S.count(jewel) for jewel in J}   
    return sum(d.values())



print(numJewelsInStones('aA','aAAbbbb'))
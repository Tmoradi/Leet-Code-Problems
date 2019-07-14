from collections import defaultdict
def distributeCandies(candies):
    # get the number of different candies
    d = {i:candies.count(i) for i in candies}
    
    for _, candy in d.items():
        if candy % 2 == 0:
            counter += 1 
    return counter 




from collections import defaultdict

def uncommonFromSentences(A,B):
    d = defaultdict(int)
    all_words = (A +' '+B).split()
    ''' 
NEED TO DO 

    '''
    for word in all_words:
            d[word] += 1
    return [word for word in all_words if d[word] == 1] 
        

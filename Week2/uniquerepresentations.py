def uniqueMorseRepresenations(words):
    # english letters for morse code 
    morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....",
    "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-","-.--","--.."]
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    # mapping between aplhabet and morsecode 
    d = {alpha:morse for (alpha,morse) in zip(alphabet,morsecode)}
'''
NEED TO DO
'''

print(uniqueMorseRepresenations(["gin", "zen", "gig", "msg"]))
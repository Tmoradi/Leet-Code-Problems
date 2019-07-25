from collections import Counter
def uniqueMorseRepresenations(words):
    # english letters for morse code 
    morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....",
    "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-","-.--","--.."]
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    unqiue_reps = set() 
    # mapping between aplhabet and morsecode 
    alpha_2_morse = {alpha:morse for (alpha,morse) in zip(alphabet,morsecode)}
    for word in words:
        temp = ''
        for letter in word:
            temp += alpha_2_morse[letter]
        unqiue_reps.add(temp)    

    return len(unqiue_reps)


print(uniqueMorseRepresenations(["gin", "zen", "gig", "msg"]))
from collections import Counter
def subdomainVisits(cpdomains):
    # first we should split up domain visits
    # with the url 
    output = []
    c = Counter()
    # Creating the dictionary
    for string in cpdomains:
        temp = string.split()
        # split the url
        temp+=string.split()[1].split('.')[1:]
        c.update(temp)
    print(c)
    

        



    return None
    
print(subdomainVisits(["9001 discuss.leetcode.com"]))
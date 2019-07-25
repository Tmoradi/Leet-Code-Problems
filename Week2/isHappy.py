def isHappy(n): 
    tracker = set()
    while True: 
        if n == 1:
            return True 
        elif n in tracker:
            return False 
        else:
            tracker.add(n)
            n = sum([int(c)**2 for c in str(n)])
   
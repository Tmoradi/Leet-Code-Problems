def lemonade_change(bills):
    #cost per drink
    cost = 5
    #amount of money we have left 
   
    # we need a counter to figure out the correct change 
    change = 0
    
    for bill in bills:
        if bill == 5:
            change+= 5
        else:
            if bill- cost == 5 and change >= 5
                change-= 5
            elif bill-cost == 15 and change >= 15
                change -= 15
    if change == 0:
        return True 
    else:
        return False 

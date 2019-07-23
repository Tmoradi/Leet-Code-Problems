
def sortArrayByParity(A):
    
    solution = []
    for value_in_a in A:
        if (value_in_a % 2 == 0):
            solution.insert(0,value_in_a)
        else:
            solution.append(value_in_a)
    return solution
    
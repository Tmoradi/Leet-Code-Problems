def calPoints(ops):
    # # need a total output 
    # out = 0
    # # to keep track of points earned in prev round 
    # stack = []

    # for char in ops:
    #     print(stack,out)
    #     if char not in "+DC":
    #         out+= int(char)
    #         stack.append(int(char))
    #     else:
    #         if char == 'D':
    #             temp = stack.pop()
    #             out += temp*2
    #             stack.append(temp)
    #             stack.append(temp*2)
    #         elif char == 'C':
    #             temp = stack.pop()
    #             out -= temp
    #         else:
    #             temp = stack.pop()
    #             temp_2 = stack.pop()
    #             out += (temp+temp_2) 
    #             stack.append(temp_2)
    #             stack.append(temp)
    #             stack.append(temp+temp_2)
    # return out 
    stack = []

    for char in ops:
        if char not in '+DC':
            stack.append(int(char))
        elif char == 'D':
            stack.append(2 * stack[-1])
        elif char == '+':
            stack.append(stack[-1]+stack[-2])
        else:
            stack.pop()
        return sum(stack)


print(calPoints(["5","-2","4","C","D","9","+","+"]))
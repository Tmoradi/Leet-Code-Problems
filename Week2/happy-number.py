
def happy_number(number):
    number_copy = str(number)
    val = None
    d = {f'char_{i}': int(char) for i,char in enumerate(number_copy)}

    # print(str(number))
    while val != 1:
        val = int(sum([x**2 for x in d.values()]))
        if (val != 1 == True):
            new_d = {f'char_{i}': int(char) for i,char in enumerate(str(val))}
            d.update(new_d)
    return True 

print(happy_number(19))
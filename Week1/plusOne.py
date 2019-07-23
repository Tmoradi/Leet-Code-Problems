
def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in range(len(digits)-1,-1,-1):
        val = digits[i] + carry
        if val > 9:
            carry = 1 
            digits[i] = 0
        else:
            carry = 0
            digits[i] = val
            break 
        if carry:
            arr = [1]
            arr.extend(digits)
            return arr        
        return digits
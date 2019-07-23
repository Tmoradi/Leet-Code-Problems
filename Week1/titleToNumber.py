
def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = range(1,27)
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter_to_num = {letters[num - 1]:num for num in nums}
        res = 0
        k = 1
        for i in xrange(len(s) - 1):
            res += k * 26
            k *= 26
        
        i = 0
        while i < len(s):
            res += k * (letter_to_num[s[i]] - 1)
            k /= 26
            i += 1
        
        return res + 1 
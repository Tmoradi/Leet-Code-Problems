
def reverseWords(self, s: str) -> str:
        # each element is a word we are going to reverse 
        answer = ''
        for word in s.split(' '):
            answer+= word[::-1] + ' '
        return answer.rstrip()

def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for value in range(1,n+1):
            
            if (value % 3 == 0 and value % 5 == 0):
                 answer.append('FizzBuzz')
            elif (value % 5 == 0):
                answer.append('Buzz')
            elif (value % 3 == 0):
                 answer.append('Fizz')
            else:
                answer.append(str(value))
        return answer
               
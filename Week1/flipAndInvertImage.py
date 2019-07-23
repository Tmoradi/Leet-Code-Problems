def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        invert = lambda x: 0 if x==1 else 1
        return [list(map(invert, item)) for item in [row[::-1] for row in A]]

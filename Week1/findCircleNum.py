
def findCircleNum(self, M: List[List[int]]):
    
        def find(x):
            if uf[x]!=x: 
                return find(uf[x])
            else: 
                return x
    
        N=len(M)
    
        uf=list(range(N))
        for i in range(N):
            for j in range(N):
                if M[i][j]:
                    uf[find(i)] = find(j)
        return len(set(find(i) for i in range(N)))
        

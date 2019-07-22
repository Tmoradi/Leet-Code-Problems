from collections import defaultdict 
def canFinish(c,p):
        g = [[] for _ in range(c)]
        v = [0 for _ in range(c)]
        for s, e in p:
            g[s] += [e]
        for r, nb in enumerate(g):
            if not dfs(g, r, v):
                return False
        return True


def dfs(self,g, r, v):
        if v[r] == -1:
            return False
        v[r] = -1
        for n in g[r]:
            if not self.dfs(g, n, v):
                return False
        v[r] = 2 
        return True

print(canFinish(2,[[1,0]]))
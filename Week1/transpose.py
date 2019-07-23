def transpose(A): 
    row = len(A)
    col = len(A[0])
    b = [[0]*row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            b[c][r] = A[r][c] 
    return b

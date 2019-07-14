def merge(intervals):
    # going to contain our list of lists 
    output = []
    sort_intervals = sorted(intervals,key=lambda x: x[0])

    
print(merge([[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]))


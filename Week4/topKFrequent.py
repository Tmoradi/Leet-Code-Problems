from collections import Counter
import heapq
def topKFrequent(nums,k):
    if len(nums) == 0 or k == 0:
        return []
    # going to need to create our dictionary and heap
    counted = Counter(nums)

    
    return heapq.nlargest(k,counted.keys,key=counted.get())
        



print(topKFrequent([4,1,-1,2,-1,2,3],2))
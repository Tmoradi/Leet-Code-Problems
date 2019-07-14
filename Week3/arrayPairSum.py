def arrayPairSum(nums):
    sorted_list = sorted(nums)
    return sum([sorted_list[i] for i in range(0,len(sorted_list)-1,2)]) 


print(arrayPairSum([1,4,3,2]))
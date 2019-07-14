def search(nums,target):
    # other version to find 
   # a target value

    # if target not in nums:
    #             return -1 
    #         return nums.index(target)


    high = len(nums) - 1 
    low = 0
    mid = high+low // 2
    if target not in nums:
        return -1
    while nums[mid] != target:
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            mid += 1
        elif nums[mid] > target:
            mid -=1
    return mid 

print(search( [-1,0,3,5,9,12],3))
print(search( [-1,0,3,5,9,12],9))
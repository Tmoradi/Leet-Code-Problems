def rotate(nums,k):

    queue = []
    for i in range(len(nums),0,-1):
        print(i)
        if len(nums) % 2 == 0:
            temp_idx = -i+k-1
            queue.append(nums[temp_idx])
        else:
            temp_idx = -i+k+1
            queue.append(nums[temp_idx])    
        print(queue)
    # this is going to adjust nums according to new idx
    for i in range(len(nums)):
        nums[i] = queue[i]
        

print(rotate([1,2],3))
# print(rotate([-1,-100,3,99],2))


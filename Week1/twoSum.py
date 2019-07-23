def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            value = nums[i]
            targ = target - value
            if targ in nums and nums.index(targ) != i: 
                output.append(i)
                output.append(nums.index(targ))
                return output
            continue 
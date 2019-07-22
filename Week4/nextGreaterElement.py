def nextGreaterElement(nums1,nums2):
    # need an output array 
    output = []
    for number in nums1: 
        temp_location = nums2.index(number)
        if temp_location == len(nums2)-1:
            output.append(-1)
        else:
            temp_array = nums2[temp_location+1:]
            if number > max(temp_array):
                output.append(-1)

            else:
                for i in range(len(temp_array)):
                    if number < temp_array[i]:
                        output.append(temp_array[i])
                        break
        return output


print(nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))
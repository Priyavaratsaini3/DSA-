def remove(nums):
    val = 3
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] == val:
            nums[l] = nums[r]
            r -= 1
        else: 
           l += 1 
    return l
print(remove(nums=[3,2,1,2,3,4]))
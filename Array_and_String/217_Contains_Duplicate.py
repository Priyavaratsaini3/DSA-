def cntainsDuplicate(nums: int):
    r = 0
    unique = set()
    while r < len(nums):
        if nums[r] not in unique:
            unique.add(nums[r])
            r += 1
            if len(nums) == len(unique):
                return False 
        else: 
            return True

print(cntainsDuplicate(nums = [1,2,3]))
nums = [1, 2, 3, 4]
k = 5

left, right = 0, len(nums) - 1
operations = 0 

while left < right:
    total = nums[left] + nums[right]
    if total == k:
        nums.pop(right)
        nums.pop(left)
        operations += 1
        print(nums)
        
        left, right = 0, len(nums) - 1

    elif total < k:
        left += 1
    else:
        right -= 1

print("Total operations performed:", operations)

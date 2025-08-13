nums = [0, 1, 0, 2, 3, 12]
left= 0

for num in nums:
    if num != 0:
        nums[left] = num
        left += 1
    
while left < len(nums):
     nums[left] = 0
     left += 1
print(nums)
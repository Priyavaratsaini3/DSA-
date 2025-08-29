nums = [1, 12, -5, -6, 50, 3]
k = 4
sum = sum(nums[:k])
max_sum = sum
l= 0 
r = k
while r < len(nums):
    sum = sum - nums[l]
    sum = sum + nums[r]
    max_sum = max(max_sum, sum)
    l += 1
    r += 1
    max_average = max_sum / k
print(max_average)
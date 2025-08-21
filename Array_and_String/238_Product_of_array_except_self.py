nums = [1,2,3,4]
# output = [24,12,8,6]
# Time complexity is O(n^2)
res = []

for i in range(len(nums)):
    current_value = nums.pop(i)  
    product = 1
    for n in nums:             
        product *= n
    res.append(product)
    nums.insert(i, current_value)       

print(res)

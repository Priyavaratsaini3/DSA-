nums = [2,3,1,2,4,3]
target = 7
minlen = float("inf")
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum = sum + nums[j]
    if sum >= target:
        minlen = min(minlen, j-i+1)
    else:
        print(0)
print(minlen)

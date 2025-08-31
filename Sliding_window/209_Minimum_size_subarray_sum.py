nums = [5,1,3,5,10,7,4,9,2,8]
target = 15
# minlen = float("inf")
# for i in range(len(nums)):
#     sum = 0
#     for j in range(i,len(nums)):
#         sum += nums[j]
#         if sum >= target:
#             minlen = min(minlen, j-i+1)
#             break
# print(minlen)
# print(sum)

l = 0 
r = 0 
minlen = float("inf")
sum = 0

while r < len(nums):
    sum += nums[r]

    while sum >= target:
        minlen = min(minlen, r - l + 1)
        sum -= nums[l]
        l += 1
    r += 1
if minlen == float("inf"):
    print(0)
else:
    print(minlen)
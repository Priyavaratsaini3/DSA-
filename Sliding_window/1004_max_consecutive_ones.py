nums = [1,1,1,0,0,0,1,1,1,1,1,1,1,0]
# output = 6
k = 2
r = 0
l = 0
maxlen = 0
count = 0

while r < len(nums):
    if  nums[r] == 0:
        count += 1
    if count > k:
        if nums[l] == 0:
            count -= 1
        l += 1
    if count <= k:
        count_of_ones = r - l + 1
        maxlen = max(maxlen, count_of_ones)
    r += 1
print(maxlen)
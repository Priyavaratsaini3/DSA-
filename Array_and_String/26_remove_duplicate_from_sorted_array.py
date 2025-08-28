def removeDuplicates(nums):
        unique_nums = set(nums)
        change_list = list(unique_nums)
        count = 0
        for i in range(len(change_list)):
            count += 1 
        return change_list

nums=1,1,2
print(removeDuplicates(nums))
# new = set(nums)
# nww = list(new)
# count = 0 
# for i in range(len(nww)):
#     count += 1
# print(count)
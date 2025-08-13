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
# def move_zeroes(nums):
#     # Pointer for position of the next non-zero element
#     insert_pos = 0
    
#     # First pass: move all non-zero elements to the front
#     for num in nums:
#         if num != 0:
#             nums[insert_pos] = num
#             insert_pos += 1
    
#     # Second pass: fill the rest with zeros
#     while insert_pos < len(nums):
#         nums[insert_pos] = 0
#         insert_pos += 1


# # Example
# nums = [0, 5, 3, 0, 7, 9]
# move_zeroes(nums)
# print(nums)  # [5, 3, 7, 9, 0, 0]

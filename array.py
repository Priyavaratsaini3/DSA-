from array import *

# val = array('i',[1,2,3,4,5,6,7,8,9] )

# for i in range(0, len(val)):
#     print(val[i] , end=" ")

# print("\n")

# for x in val:
#     print(x, end=" , ")

# print("\n")
# print(val.typecode)

# val.reverse()

# val.insert(1,50)
# val.append(399)
# val[3] = 400

# copyArray = array(val.typecode, (x*2 for x in val))

# copyArray.pop(3)
# copyArray.remove(10)

# abc = val[2: -3]
# abc.reverse()
# for i in range(0,len(abc)):
#     print(abc[i], end=" ")

# arr = array('i',[])
# print("\n")

# n = int(input("Enter a number: "))

# for i in range(0,n):
#     arr.append(int(input("Enter next input: ")))

# for x in arr:
#     print(x, end=" ")

# i = val.index(5)
# print(i)

from numpy import *
# arr = array([1,2,3,4,5.0, "h"])
# arr = array([1,2,3,4], float)
# arr = linspace(5,20,4)
# arr = arange(10,20,2)
# arr = logspace(10,20,2)
# arr = zeros(10)
# arr = ones(10)
# arr = full(10, 2)
# print(arr)

# for i in arr:
#     print(i, end=" ")

# zero = array(10)
# print(zero)

# one = array([1,2,3,4])
# print(one)

# two = array([[1,2,3], [12, 3,4], [1,2,3]])
# print(two)

# three = array([[[1,2,3,4]], [[1,2,3,4]], [[1,2,3,4]]])
# print(three)
# print(shape(three))
# print(three.dtype)

# def arrSearching():
#     arr = [1,2,3,4]
#     x = 3
#     if x in arr:
#         return arr.index(x)
#     else: 
#         return -1
    
# print(arrSearching())

# def arrMinMax():
#     new = list()
#     arr = [1,2,3,4,64,66, 100, 101, 1000, 99 ,10]
#     arr.sort()
#     new.append(arr[0])
#     new.append(arr[-1])
#     return new
# print(arrMinMax())

# def arrMinMax():
#     arr = [1,3,4,5,6,7,7,5,5,555]
#     min = arr[0]
#     max = arr[0]
#     new = list()

#     for i in range(0, len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#         if arr[i] > max:
#             max = arr[i]
#     new.append(min)
#     new.append(max)
#     return new

# print(arrMinMax())

# def missingarr():
#     arr = [1,2,3,4,5,6,7,8,10,11,12]

#     n = len(arr)
#     new1 = n+1
#     print(n)
#     sum = 0
#     new = 0
   
#     for i in range(n):
#         sum += arr[i]
#     for j in range(1,new1+1):
#         new += j
#     return new - sum
# print(missingarr())

# Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
# Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

# Note: It is guaranteed that the array contains exactly one bitonic point.

# Examples:

# Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 8
# Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].
# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 50
# Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.
# Input: arr[] = [120, 100, 80, 20, 0]
# Output: 120
# Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].
# Constraints:
# 3 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 106

def arrMaximum():
    arr = [1,2,4,5,7,8,3]
    max = arr[0]
    

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
    
print(arrMaximum())
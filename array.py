from array import *

val = array('i',[1,2,3,4,5,6,7,8,9] )

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

i = val.index(5)
print(i)

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

zero = array(10)
print(zero)

one = array([1,2,3,4])
print(one)

two = array([[1,2,3], [12, 3,4], [1,2,3]])
print(two)

three = array([[[1,2,3,4]], [[1,2,3,4]], [[1,2,3,4]]])
print(three)
print(shape(three))
print(three.dtype)
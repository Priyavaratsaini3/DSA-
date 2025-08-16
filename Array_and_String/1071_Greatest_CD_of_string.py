import math
str1 = "ABABAB"
str2 = "ABAB"
# output = "ABC"
str_copy = str1.upper()

xr = math.gcd(len(str_copy), len(str2))
# print(str1[:xr])
print(xr)

# n = 123123123
# r = 123

# xr = math.gcd(n, r)
# print(xr)

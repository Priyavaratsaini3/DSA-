import math 
def power(n):
    if n > 0 and (n & (n - 1)) == 0:
        return True 
    else:
        return False
print(power(1))
digits = [9]
# output = [1,2,4]
digits[-1] = digits[-1] + 1

n = digits.pop()

for i in str(n):
    digits.append(int(n))

print(digits)
n = 7
# output = True
# 1^2 + 9^2 = 82
unique_numbers = set()
while n != 1 and n not in unique_numbers:
    unique_numbers.add(n)
    sum = 0
    for i in str(n):
        sum += int(i)**2
    print(sum)
    n = sum
if n == 1:
    print(True)
else:
    print(False)
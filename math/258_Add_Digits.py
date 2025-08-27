def new(num):
# output = 2
    while num >= 10:
        sum = 0
        for i in str(num):
            sum += int(i)
        num = sum
    return num
print(new(222222))
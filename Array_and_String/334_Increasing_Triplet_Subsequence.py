num =[2,1,5,0,4,6]
first = float('inf')
second = first
for n in num:
    if n <= first:
        first = n
    elif n <= second:
        second = n 
    else:
        print(True)



    
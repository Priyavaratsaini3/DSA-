flowerbed = [1,0,0,0,1]
n = 1
count = 0
for i in range(len(flowerbed)):
    if flowerbed[i] == 0:

        left = (i == 0) or (flowerbed[i - 1] == 0)

        right = (i == len(flowerbed)- 1) or flowerbed[i + 1] == 0

        if left and right:
            flowerbed[i] = 1
            count += 1

            if  count >= n:
                print(True)
    
print(count>= n)

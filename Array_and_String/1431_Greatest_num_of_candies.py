def GreatestNumberofCandies(candies, extra_candies):
    output = []
    max_candies = max(candies)
    for i in candies:
        sum = extra_candies + i
        if sum >= max_candies:
            output.append(True)
        else: 
            output.append(False)
    return output
print(GreatestNumberofCandies(candies = [2,3,5,1,3],extra_candies = 3))
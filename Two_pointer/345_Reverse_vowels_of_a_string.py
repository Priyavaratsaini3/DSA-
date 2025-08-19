s = "IceCreAm"
s = list(s)
t = "aeiouAEIOU"
left, right = 0, len(s) - 1

while left < right:
    if s[left] not in t:
        left += 1
    elif s[right] not in t:
        right -= 1
    else:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

reverse = "".join(s)
print(reverse)

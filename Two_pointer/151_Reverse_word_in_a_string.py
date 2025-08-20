s = "the sky is blue"
# o = "blue is sky the"
s = s.split()
print(s)
left , right = 0 , len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    if left < right:
        left += 1
        right -= 1

o = " ".join(s)
print(o)
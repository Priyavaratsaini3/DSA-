s = "abciiidef"
k = 3
t = "aeiou"
l = 0
r = 0
count = 0
max_vowels = 0

while r < len(s):
    if s[r] in t:
        count += 1
    
    if r - l + 1 > k:
        if s[l] in t:
            count -= 1
        l += 1
    max_vowels = max(max_vowels, count)        
    r += 1
print(max_vowels)
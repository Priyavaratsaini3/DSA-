text = "hello world"
brokenLetters = "sd"
count = 0
max_count = 0
word = text.split()
for w in word:
    if any(ch in w for ch in brokenLetters):
        continue
    count += 1
max_count = max(max_count, count)
print(max_count)
def isSubsequence(s, t):
        left, right = 0, 0 

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1          
            right += 1              

        return left == len(s)

print(isSubsequence(s = "abc", t = "ahbgdc"))
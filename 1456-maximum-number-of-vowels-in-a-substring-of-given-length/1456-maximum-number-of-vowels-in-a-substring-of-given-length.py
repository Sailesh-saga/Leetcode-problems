class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        c=0
        m=0
        for right in range(len(s)):
            if s[right] in "aeiou":
                c+=1
            if right>=k-1:
                m=max(m,c)
                if s[left] in "aeiou":
                    c-=1
                left+=1
        return m
        
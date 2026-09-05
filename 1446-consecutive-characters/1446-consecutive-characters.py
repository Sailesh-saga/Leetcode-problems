class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        a=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
                a.append(c)
            else:
                c=1
        if a==[]:
            return 1
        else:
            return max(a)
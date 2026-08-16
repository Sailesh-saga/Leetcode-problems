class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
        a=[]
        for i in d:
            if(d[i]%2!=0):
                a.append(d[i]-1)
            else:
                a.append(d[i])
        if(len(s)>sum(a)):
            return sum(a)+1
        else:
            return sum(a)
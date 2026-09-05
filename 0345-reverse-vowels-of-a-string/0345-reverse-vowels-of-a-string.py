class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        alpha=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        while(l<r):
            if (s[l] in alpha) and (s[r] in alpha):
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] not in alpha:
                l+=1
            elif s[r] not in alpha:
                r-=1
        return "".join(s)



                
            


        
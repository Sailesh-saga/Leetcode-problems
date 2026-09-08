class Solution:
    def countCommas(self, n: int) -> int:
        if int(log10(n) + 1) <=3:
            return 0
        else:
            c,d,e=0,0,0
            
            for i in range(1000,n+1):
                c+=1
            if n<=10**5:
                return c
            elif n>10**5 + 1 and n<=10**9:
                num=99001 + ((c-99001)*2)
                return num
                
            
        
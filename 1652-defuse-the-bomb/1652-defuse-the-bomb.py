class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        a=[]
        for i in range(len(code)):
            a.append(code[i])
        for i in range(len(code)):
            a.append(code[i])
        for i in range(len(code)):
            a.append(code[i])
        c=[]
        if k>0:
            for i in range(len(code),len(code)*2):
                s=sum(a[i+1:i+k+1])
                c.append(s)
        else:
            for i in range(len(code),len(code)*2):
                b=abs(k)
                d=sum(a[i-b:i])
                c.append(d)
        return c
        
        
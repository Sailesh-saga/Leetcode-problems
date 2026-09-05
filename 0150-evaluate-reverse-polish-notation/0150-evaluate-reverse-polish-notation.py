class Solution:
    def evalRPN(self, t: List[str]) -> int:
        a=[]
        for i in range(len(t)):
            if(t[i]=='+'):
                s=a[-1]+a[-2]
                a.pop()
                a.pop()
                a.append(s)
            elif(t[i]=='-'):
                b=a[-2]-a[-1]
                a.pop()
                a.pop()
                a.append(b)
            elif(t[i]=='*'):
                c=a[-1] * a[-2]
                a.pop()
                a.pop()
                a.append(c)
            elif(t[i]=='/'):
                d=int(a[-2]/a[-1])
                a.pop()
                a.pop()
                a.append(d)
            else:
                a.append(int(t[i]))
        return a[0]
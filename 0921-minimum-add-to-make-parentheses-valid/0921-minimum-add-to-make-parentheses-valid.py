class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        c=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')' and len(stack)>0:
                stack.pop()
            else:
                c+=1
        return len(stack)+c

        
        
                

        
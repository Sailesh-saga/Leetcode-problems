class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(list(s1))
        k=len(s1)
        left=0
        s3=[]
        c=0
        for right in range(len(s2)):
            s3.append(s2[right])
            if right>=k-1:
                if sorted(s3)==s1:
                    c+=1
                s3.remove(s2[left])
                left+=1
        return c>0
        
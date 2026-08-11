class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        for i in range(len(s1)):
            d[s1[i]]=d.get(s1[i],0)+1
        l=0
        d1={}
        k=len(s1)
        c=0
        for i in range(len(s2)):
            d1[s2[i]]=d1.get(s2[i],0)+1
            if(i>=k):
                d1[s2[l]]-=1
                if(d1[s2[l]]==0):
                    del d1[s2[l]]
                l+=1
            if(d1==d):
                c+=1
        return c>0
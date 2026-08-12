class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict1={}
        for i in p:
            dict1[i]=dict1.get(i,0)+1
        k=len(p)
        left=0
        dict2={}
        a=[]
        c=[]
        for right in range(len(s)):
            dict2[s[right]]=dict2.get(s[right],0)+1
            if right>=k-1:
                if dict1==dict2:
                    a.append(left)    
                dict2[s[left]]-=1
                if dict2[s[left]]==0:
                    del dict2[s[left]]
                left+=1
        return a

        
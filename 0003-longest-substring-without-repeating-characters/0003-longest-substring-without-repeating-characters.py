class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1={}
        m=0
        left=0
        for right in range(len(s)):
            while(s[right] in dict1):
                dict1[s[left]]-=1
                if dict1[s[left]]==0:
                    dict1.pop(s[left])
                left+=1
            dict1[s[right]]=dict1.get(s[right],0)+1
            m=max(m,right-left+1)
        return m
        
        
       
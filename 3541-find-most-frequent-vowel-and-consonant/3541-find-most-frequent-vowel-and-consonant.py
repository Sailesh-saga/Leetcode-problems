class Solution:
    def maxFreqSum(self, s: str) -> int:
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i]=0
            dict1[i]+=1
        maxi,maxi1=0,0
        for i in dict1:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                if(dict1[i]>=maxi):
                    maxi=dict1[i]
            else:
                if(dict1[i]>=maxi1):
                    maxi1=dict1[i]
        return maxi1+maxi
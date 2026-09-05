class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c=1
        m=0
        a=[]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c+=1
                a.append(c)
            else:
                c=1
        if a==[]:
            return 1
        else:
            return max(a)
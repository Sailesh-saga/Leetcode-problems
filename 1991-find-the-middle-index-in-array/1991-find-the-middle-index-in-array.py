class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        a=[0]*len(nums)
        b=[0]*len(nums)
        s=0
        for i in range(len(nums)):
            a[i]=s
            s+=nums[i]
        s1=0
        for i in range(len(nums)-1,-1,-1):
            b[i]=s1
            s1+=nums[i]
        c=-1
        for i in range(len(a)):
            if a[i]==b[i]:
                c=i
                break
        return c
        
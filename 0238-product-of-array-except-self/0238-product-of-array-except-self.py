class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            r[i]=pre
            pre*=nums[i]
        suff=1
        for i in range(n-1,-1,-1):
            r[i]*=suff
            suff*=nums[i]
        return r
        
        
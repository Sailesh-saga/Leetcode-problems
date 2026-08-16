class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=nums[0]
        s=nums[0]
        for i in range(1,len(nums)):
            m=max(m+nums[i],nums[i])
            s=max(s,m)
        return s
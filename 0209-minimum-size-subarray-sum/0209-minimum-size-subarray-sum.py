class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        currsum=0
        m=1000000000
        for right in range(len(nums)):
            currsum+=nums[right]
            while currsum>=target and left<=right:
                m=min(m,right-left + 1)
                currsum-=nums[left]
                left+=1
        if m==1000000000:
            return 0
        else:
            return m
        
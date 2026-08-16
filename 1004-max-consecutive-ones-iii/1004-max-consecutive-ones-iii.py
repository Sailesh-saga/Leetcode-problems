class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zc=0
        left=0
        m=0
        for right in range(len(nums)):
            if nums[right]==0:
                zc+=1
            while(zc>k):
                if nums[left]==0:
                    zc-=1
                left+=1
            m=max(right-left+1,m)
        return m
        
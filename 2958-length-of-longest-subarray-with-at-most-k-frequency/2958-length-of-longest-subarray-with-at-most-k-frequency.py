class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dict1={}
        left=0
        m=0
        ma=0
        for right in range(len(nums)):
            dict1[nums[right]]=dict1.get(nums[right],0)+1
            while(dict1[nums[right]]>k):
                dict1[nums[left]]-=1
                left+=1
            ma=max(ma,right-left+1)
        return ma
        
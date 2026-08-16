class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        c=0
        while(i<len(nums)-1 and j<len(nums)):
            if nums[i]==nums[j]:
                j+=1
            else:
                i=i+1
                nums[i]=nums[j]
        return i + 1
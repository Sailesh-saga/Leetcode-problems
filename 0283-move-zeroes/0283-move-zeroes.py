class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        for i in range(len(nums)):
            if(nums[i]==0):
                continue
            else:
                temp=nums[c]
                nums[c]=nums[i]
                nums[i]=temp
                c+=1
        return nums

        
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        curr_sum=0
        avg=-1*(10**4)
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if i>=k-1:
                avg1=curr_sum/k
                avg=max(avg1,avg)
                curr_sum-=nums[left]
                left+=1
        return avg
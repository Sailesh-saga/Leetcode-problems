class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        a=[-1]*n
        window_size=2*k + 1
        if window_size>n:
            return a
        window_sum=sum(nums[:window_size])
        avg=window_sum//window_size
        a[k]=avg
        for right in range(k+1,n-k):
            window_sum+=nums[right+k]
            window_sum-=nums[right-k-1]
            avg=window_sum//window_size
            a[right]=avg
        return a

        
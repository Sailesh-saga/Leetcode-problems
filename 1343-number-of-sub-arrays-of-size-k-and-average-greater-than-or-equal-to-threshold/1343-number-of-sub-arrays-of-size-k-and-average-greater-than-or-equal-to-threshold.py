class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        curr_sum=0
        c=0
        for right in range(len(arr)):
            curr_sum+=arr[right]
            if right>=k-1:
                avg=curr_sum//k
                if avg>=threshold:
                    c+=1
                curr_sum-=arr[left]
                left+=1
        return c
        
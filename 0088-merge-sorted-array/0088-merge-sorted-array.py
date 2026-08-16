class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j=0
        for i in range(m,m+n):
            nums1[i]=nums2[j]
            j+=1
        for i in range(len(nums1)):
            for j in range(len(nums1)-1):
                if nums1[j]>nums1[j+1]:
                    temp=nums1[j]
                    nums1[j]=nums1[j+1]
                    nums1[j+1]=temp
        return nums1
        
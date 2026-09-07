class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        for i in range(len(nums2)-1):
            m=nums2[i]
            for j in range(i+1,len(nums2)):
                m=max(m,nums2[j])
                if m!=nums2[i]:
                    break
            if m==nums2[i]:
                dict1[nums2[i]]=-1
            else:
                dict1[nums2[i]]=m
        dict1[nums2[-1]]=-1
        a=[]
        for i in nums1:
            if i in dict1:
                a.append(dict1[i])
        return a
        
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a=sorted(nums)
        c=[]
        se=set()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while(l<r):
                s=a[i]+a[l]+a[r]
                if s==0:
                    se.add((a[i],a[l],a[r]))
                    l+=1
                    r-=1
                elif s>0:
                    r-=1
                else:
                    l+=1
        return list(se)

                
                
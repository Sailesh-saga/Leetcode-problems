class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        c=0
        while(i<j):
            m=min(height[i],height[j])
            a=m*(j-i)
            c=max(c,a)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return c
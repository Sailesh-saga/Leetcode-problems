class Solution:
    def largestCombination(self, ci: List[int]) -> int:
        m=0
        n=len(ci)
        for mask in range(24):
            c=0
            for i in range(n):
                if(ci[i]&(1<<mask))>0:
                    c+=1
            m=max(m,c)
        return m

        


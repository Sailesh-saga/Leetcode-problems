class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[]
        c=0
        for i in range(len(gain)):
            a.append(c)
            c+=gain[i]
        a.append(c)
        return max(a)
        
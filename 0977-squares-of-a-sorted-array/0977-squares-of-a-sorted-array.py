class Solution:
    def sortedSquares(self, num: List[int]) -> List[int]:
        for i in range(len(num)):
            num[i]=num[i]**2
        return sorted(num)
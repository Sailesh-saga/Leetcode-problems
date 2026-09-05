class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        for i in candies:
            a.append(i+extraCandies>=max(candies))
        return a

        
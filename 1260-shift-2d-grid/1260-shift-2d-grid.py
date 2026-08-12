class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                a.append(grid[i][j])
        i=1
        k=k%(len(grid)*len(grid[0]))
        a=a[-k:]+a[:-k]
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j]=a[c]
                c+=1
        return grid

        
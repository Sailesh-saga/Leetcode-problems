class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        b=[]
        for i in range(len(matrix)):
            a=[]
            for j in range(len(matrix[i])):
                a.append(matrix[j][i])
            b.append(list(reversed(a)))
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         matrix[i][j]=b[i][j]
        matrix[:]=b
       


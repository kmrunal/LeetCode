# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# example
# Input
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# output
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Input
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]

# output

# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# Approach 1 : Transpose and then reverse
# The obvious idea would be to transpose the matrix first and then reverse each row.

# Time complexity : O(N ** 2)
# Space complexity: O(1)



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

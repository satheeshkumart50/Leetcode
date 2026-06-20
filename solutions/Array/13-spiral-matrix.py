# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Time Complexity - O(m*n) where m is the number of rows and n is the number of columns in the matrix
# Space Complexity - O(m*n) for the output list and O(1) for the pointers and variables used in the algorithm
# Category - Array
# Hint - Use four pointers to keep track of the boundaries of the matrix, left, right, top and bottom, we can iterate through the matrix in a spiral manner by moving the pointers accordingly, we can use a while loop that continues until the length of the output list is less than the total number of elements in the matrix, in each iteration we can move right, down, left and up and update the pointers accordingly, at the end we return the output list which will contain the elements in spiral order
    # Refer - video - https://www.youtube.com/watch?v=3Zv-s9UUrFM

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        spiral_lst = []

        while len(spiral_lst) < (len(matrix) * len(matrix[0])):

            for i in range(left, right + 1):
                spiral_lst.append(matrix[top][i])

            # important to check the length of spiral_lst after each direction to avoid adding duplicate elements when there is only one row left in the matrix
            if len(spiral_lst) == (len(matrix) * len(matrix[0])):
                break

            top += 1

            for j in range(top, bottom + 1):
                spiral_lst.append(matrix[j][right])

            right -= 1

            for k in range(right, left - 1, -1):
                spiral_lst.append(matrix[bottom][k])

            # important to check the length of spiral_lst after each direction to avoid adding duplicate elements when there is only one column left in the matrix
            if len(spiral_lst) == (len(matrix) * len(matrix[0])):
                break

            bottom -= 1

            for l in range(bottom, top - 1, -1):
                spiral_lst.append(matrix[l][left])

            left += 1

        return spiral_lst
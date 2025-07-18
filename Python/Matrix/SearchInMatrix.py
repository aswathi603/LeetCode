# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-matrix-1587115621
# Search in a sorted Matrix
# Difficulty: MediumAccuracy: 56.27%Submissions: 138K+Points: 4
# Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
# Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

# Examples:

# Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
# Output: true
# Explanation: 14 is present in the matrix, so output is true.
# Input: mat[][] = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42
# Output: false
# Explanation: 42 is not present in the matrix.
# Input: mat[][] = [[87, 96, 99], [101, 103, 111]], x = 101
# Output: true
# Explanation: 101 is present in the matrix.
# Constraints:
# 1 <= n, m <= 1000
# 1 <= mat[i][j] <= 109
# 1 <= x <= 109

# Expected Complexities
# Time Complexity: O(log(n×m))
# Auxiliary Space: O(1)


#User function Template for python3
import collections
class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # code here 
        n = len(mat)
        if n == 0:
            return False

        m = len(mat[0])
        if m == 0:
            return False

        low = 0
        high = (n * m) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Convert 1D index to 2D coordinates
            row = mid // m
            col = mid % m

            current_value = mat[row][col]

            if current_value == x:
                return True
            elif current_value < x:
                low = mid + 1
            else:  # current_value > x
                high = mid - 1

        return False

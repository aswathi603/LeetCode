'''
Question Link : https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Q84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
from git import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                maxArea = max( maxArea , height * width )
            stack.append(i)
        return maxArea
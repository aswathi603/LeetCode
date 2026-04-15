'''
Question Link :  https://www.geeksforgeeks.org/problems/height-of-binary-tree/1

Height of Binary Tree
Difficulty: EasyAccuracy: 78.58%Submissions: 355K+Points: 2Average Time: 15m
Given the root of a binary tree, your task is to find the maximum depth of the tree.

Note: The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

Examples:

Input: root = [12, 8, 18, 5, 11]

Output: 2
Explanation: One of the longest path from the root(node 12) goes through node 8 to node 5, which has 2 edges.
Input: root = [1, 2, 3, 4, N, 10, 5, N, N, N, N, 6, 7]

Output: 3
Explanation: The longest path from the root(node 1) to a leaf node 6 with 3 edges.
Constraints:
1 ≤ number of nodes ≤ 3*104
0 ≤ node->data ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)

'''



# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def height(self, root):
        # code here
        if root is None:
            return -1
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1
'''
Question Link : https://practice.geeksforgeeks.org/problems/level-order-traversal/1

Level order traversal
Difficulty: MediumAccuracy: 70.31%Submissions: 255K+Points: 4Average Time: 20m
Given the root of a Binary Tree, your task is to return its Level Order Traversal.

Note: A level order traversal is a breadth-first search (BFS) of the tree. It visits nodes level by level, starting from the root, and processes all nodes from left to right within each level before moving to the next.

Examples:

Input: root = [1, 2, 3]

Output: [[1], [2, 3]]
Explanation: We start with the root node 1, so the first level of the traversal is [1]. Then we move to its children 2 and 3, which form the next level, giving the final output [[1], [2, 3]].
Input: root = [10, 20, 30, 40, 50]

Output: [[10], [20, 30], [40, 50]]
Explanation: We begin with the root node 10, which forms the first level as [10]. Its children 20 and 30 make up the second level, and their children 40 and 50 form the third level, resulting in [[10], [20, 30], [40, 50]].
Constraints:
1 ≤ number of nodes ≤ 3*104
0 ≤ node->data ≤ 109

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)


'''

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        # code here
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
    
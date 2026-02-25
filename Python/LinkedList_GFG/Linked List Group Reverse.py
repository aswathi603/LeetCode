'''
Question Link :  https://leetcode.com/problems/reverse-linked-list-ii/description/

Linked List Group Reverse
Difficulty: HardAccuracy: 57.08%Submissions: 272K+Points: 8Average Time: 30m
You are given the head of a Singly linked list. You have to reverse every k node in the linked list and return the head of the modified list.
Note: If the number of nodes is not a multiple of k then the left-out nodes at the end, should be considered as a group and must be reversed.

Examples:

Input: k = 2,
   head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5
Explanation: Linked List is reversed in a group of size k = 2.
    head -> 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL


Input: k = 4,   
   head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Output: 4 -> 3 -> 2 -> 1 -> 6 -> 5
Explanation: Linked List is reversed in a group of size k = 4.
    head -> 4 -> 3 -> 2 -> 1 -> 6 -> 5 -> NULL

Constraints:
1 ≤ size of linked list ≤ 105
0 ≤ node->data ≤ 106
1 ≤ k ≤ size of linked list 
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

'''


# Solution 1: Iterative
# time complexity: O(n)
# space complexity: O(1)
"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        curr = head
        prev = None
        nextNode  = None 
        count = 0
        
        while curr and count < k:
            nextNode = curr.next
            curr.next = prev
            prev = curr 
            curr = nextNode
            count += 1
            
        if nextNode:
            head.next = self.reverseKGroup(nextNode,k)
            
        return prev
'''
GFG Question : https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
Reverse a linked list
You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.

Examples:

Input: head -> 1 -> 2 -> 3 -> 4 - > NULL
      
Output: head -> 4 -> 3 -> 2 -> 1 -> NULL
      
Input: head - >2 -> 7 -> 10 -> 9 -> 8 -> NULL
      
Output: head -> 8 -> 9 -> 10 -> 7 -> 2 -> NULL
      
Input: head -> 8 -> NULL
      
Output: head -> 8 -> NULL

       
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)


'''

from typing import Optional


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        # Code here
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
    
        return newHead
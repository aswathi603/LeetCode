'''
Question Link : https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1

Rotated a Linked List
You are given the head of a singly linked list, you have to left rotate the linked list k times. Return the head of the modified linked list.

Examples:

Input: k = 4,
   head -> 10 -> 20 -> 30 -> 40 -> 50 -> NULL
Output: 50 -> 10 -> 20 -> 30 -> 40
Explanation:
Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
Rotate 4: 50 -> 10 -> 20 -> 30 -> 40
   
Input: k = 6,
   head -> 10 -> 20 -> 30 -> 40 -> NULL
Output: 30 -> 40 -> 10 -> 20 
   
Constraints:
1 ≤ number of nodes ≤ 105
0 ≤ k ≤ 109
0 ≤ node.data ≤ 109

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

'''

from typing import Optional
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        # code here
        if not head or not head.next or k == 0:
            return head

        # Step 1: find length
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        # Step 2: reduce k
        k = k % length
        if k == 0:
            return head

        # Step 3: find k-th node
        curr = head
        for _ in range(k - 1):
            curr = curr.next

        # Step 4: rotate
        new_head = curr.next
        curr.next = None

        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head
        return new_head


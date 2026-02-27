'''
Question Link : https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1


Remove loop in Linked List
Difficulty: MediumAccuracy: 27.66%Submissions: 550K+Points: 4Average Time: 45m
Given the head of a singly linked list, the task is to remove a cycle if present. A cycle exists when a node's next pointer points back to a previous node, forming a loop. Internally, a variable pos denotes the index of the node where the cycle starts, but it is not passed as a parameter. The terminal will print true if a cycle is removed otherwise, it will print false.

Example 1:

    head -> 1 -> 3 -> 4
                 |    |
                 ------

Input: head = 1 -> 3 -> 4, pos = 2
Output: true
Explanation: The linked list looks like A loop is present in the list, and it is removed.


Example 2:

        head -> 1 -> 8 -> 3 -> 4

Input: head = 1 -> 8 -> 3 -> 4, pos = 0
Output: true
Explanation: The Linked list does not contains any loop. 


Example 3:

        head -> 1 -> 2 -> 3 -> 4
                |              |
                ----------------

Input: head = 1 -> 2 -> 3 -> 4, pos = 1
Output: true
Explanation: The linked list looks like A loop is present in the list, and it is removed.


Constraints:
1 ≤ size of linked list ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)


'''

# node class:
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val


class Solution:
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        # Step 1: Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # No loop found
        if slow != fast:
            return
        
        # Step 2: Find start of loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Step 3: Remove loop
        while fast.next != slow:
            fast = fast.next
        
        fast.next = None
        
        
        
        
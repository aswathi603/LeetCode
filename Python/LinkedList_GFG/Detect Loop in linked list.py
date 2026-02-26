'''
Question Link : https://geeksforgeeks.org/problems/detect-loop-in-linked-list/1


Detect Loop in linked list
Difficulty: MediumAccuracy: 43.49%Submissions: 517K+Points: 4Average Time: 20m
You are given the head of a singly linked list. You have to determine whether the given linked list contains a loop or not. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null. Note that pos is not passed as a parameter.

Examples:

Input: pos = 2,
    head -> 1 -> 3 -> 4
            |         |
            -----------
Output: true
Explanation: There exists a loop as last node is connected back to the second node.


Input: pos = 0,
    head -> 1 -> 8 -> 3 -> 4 -> NULL
Output: false
Explanation: There exists no loop in given linked list.


Input: pos = 1,
    head -> 1 -> 7 -> 8 -> 10
            |              |
            ----------------
Output: true
Explanation: There exists a loop as last node is connected back to the first node.
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 103       
0 ≤ pos ≤ number of nodes



'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def detectLoop(self, head):
        # code here
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps

            if slow == fast:
                return True           # loop detected

        return False  
        

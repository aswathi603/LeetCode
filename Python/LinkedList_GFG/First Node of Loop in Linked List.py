'''
Question Link : https://practice.geeksforgeeks.org/problems/find-first-node-of-loop-in-linked-list/1

You are given the head of a singly linked list. If a loop is present in the linked list then return the first node of the loop else return -1.

Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

Examples:

Input: pos = 2,
   head -> 1 ->  3 -> 2 -> 4 -> 5
                 |              |
                 ----------------


Output: 3
Explanation: We can see that there exists a loop in the given linked list and the first node of the loop is 3.



Input: pos = 0,
   head -> 1 -> 3 -> 2 -> 1 -> NULL
Output: -1
Explanation: No loop exists in the above linked list. So the output is -1.


Constraints:
1 ≤ no. of nodes ≤ 106
1 ≤ node->data ≤ 106 

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)



'''


class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None


class Solution:
    def cycleStart(self, head):
        #code here
        if not head or not head.next:
            return -1
            
        slow = head 
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast :
                break
        else:
            return -1
                
        slow = head
        while slow != fast:
            slow =slow.next
            fast = fast.next
            
        return slow.data
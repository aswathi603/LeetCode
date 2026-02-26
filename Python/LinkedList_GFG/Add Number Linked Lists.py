'''

Question Link : https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

Add Number Linked Lists
Difficulty: MediumAccuracy: 34.52%Submissions: 380K+Points: 4Average Time: 30m
You are given the head of two singly linked lists head1 and head2 representing two non-negative integers. You have to return the head of the linked list representing the sum of these two numbers.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: 
    
Output:  1 -> 1 -> 2 -> 2
Explanation: Given numbers are 123 and 999. There sum is 1122.
    
Input: 
    
Output: 7 -> 0 
Explanation: Given numbers are 63 and 7. There sum is 70.
    
Constraints:
1 ≤ Number of nodes in head1, head2 ≤ 105
0 ≤ node->data ≤ 9

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(1)


'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def addTwoLists(self, head1, head2):
        # Step 1: Reverse both lists
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        # Step 2: Add digits
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = Node(total % 10)
            curr = curr.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        # Step 3: Reverse result
        result = self.reverse(dummy.next)

        # Step 4: REMOVE LEADING ZEROS
        while result and result.data == 0:
            result = result.next

        # If all digits were zero
        return result if result else Node(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
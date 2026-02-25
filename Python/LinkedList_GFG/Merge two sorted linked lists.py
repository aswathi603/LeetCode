'''
GFG

Question Link : https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1 

Merge two sorted linked lists
Difficulty: MediumAccuracy: 62.91%Submissions: 206K+Points: 4Average Time: 30m
Given the head of two sorted linked lists consisting of nodes respectively. Merge both lists and return the head of the sorted merged list.

Examples:

Input:
    head1 -> 5 -> 10 -> 15 -> 40 -> NULL
    head2 -> 2 -> 3 -> 20 -> NULL
  
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
Explanation:
              head -> 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40 -> NULL
   
Input:
    head1 -> 1 -> 1 -> NULL
    head2 -> 2 -> 4 -> NULL 
  
Output: 1 -> 1 -> 2 -> 4
Explanation:
                head -> 1 -> 1 -> 2 -> 4 -> NULL
  
Constraints:
1 ≤ list1.size, list2.size ≤ 103
0 ≤ node->data ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

'''

# Solution :


class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        dummy = Node(-1)
        tail = dummy

        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        # Attach remaining nodes
        if head1:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next
        
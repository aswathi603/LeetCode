/*

Merge K sorted linked lists
Given an array arr[] of n sorted linked lists of different sizes. Your task is to merge all these lists into a single sorted linked list and return the head of the merged list.

Examples:

Input:
        head1 -> 1 -> 3 -> 7 -> NULL
        head2 -> 2 -> 4 -> 8 -> NULL
        head3 -> 9 -> NULL
Output: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
Explanation: The arr[] has 3 sorted linked list of size 3, 3, 1.
1st list: 1 -> 3 -> 7
2nd list: 2 -> 4 -> 8
3rd list: 9
The merged list will be: 
    
Input:
        head1 -> 1 -> 3 -> NULL
        head2 -> 8 -> NULL
        head3 -> 4 -> 5 -> 6 -> NULL
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
Explanation: The arr[] has 3 sorted linked list of size 2, 1, 3.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be: 
    
Constraints
1 ≤ total no. of nodes ≤ 105
1 ≤ node->data ≤ 103

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)


*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int x) : data(x), next(nullptr) {}
};

class Solution {
public:
    Node* mergeKLists(vector<Node*> arr) {
        
        auto cmp = [](pair<int, pair<int, Node*>> a, pair<int, pair<int, Node*>> b) {
            return a.first > b.first;
        };
        priority_queue<pair<int, pair<int, Node*>>, vector<pair<int, pair<int, Node*>>>, decltype(cmp)> min_heap(cmp);
        
        // Step 1: push heads
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i]) {
                min_heap.push({arr[i]->data, {i, arr[i]}});
            }
        }
        
        // Dummy node
        Node* dummy = new Node(0);
        Node* current = dummy;
        
        // Step 2: process heap
        while (!min_heap.empty()) {
            
            auto [val, p] = min_heap.top();
            auto [i, node] = p;
            min_heap.pop();
            
            current->next = node;
            current = current->next;
            
            if (node->next) {
                min_heap.push({node->next->data, {i, node->next}});
            }
        }
        
        return dummy->next;
    }
};

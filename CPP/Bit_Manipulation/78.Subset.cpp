/*

Code
Accepted
Accepted
Testcase
Testcase
Test Result
78. Subsets
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void allSubsets(vector<int> &nums, int index,vector<int> &subset, vector<vector<int>> &res){
        if( index == nums.size()){
            res.push_back(subset);
            return;
        }

        //pick
        subset.push_back(nums[index]);
        allSubsets(nums,index+1,subset,res);

        //returning and not pick
        subset.pop_back();
        allSubsets(nums,index+1,subset,res);
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> subset;
        vector<vector<int>> res;
        allSubsets(nums,0,subset,res);
        return res;
    }
};
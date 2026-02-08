// 368. Largest Divisible Subset
// Medium

// Given a set of distinct positive integers nums, 
// return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

// answer[i] % answer[j] == 0, or
// answer[j] % answer[i] == 0
// If there are multiple solutions, return any of them.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: [1,2]
// Explanation: [1,3] is also accepted.
// Example 2:

// Input: nums = [1,2,4,8]
// Output: [1,2,4,8]
 

// Constraints:

// 1 <= nums.length <= 1000
// 1 <= nums[i] <= 2 * 109
// All the integers in nums are unique.

#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
        vector<int> bestSubset; 
    
        void solve(vector<int>& nums, vector<int>& temp, int index) {
            // Store the bestCase so far
            if (temp.size() > bestSubset.size()) {
                bestSubset = temp;
            }
    
            for (int i = index; i < nums.size(); i++) {
                if (temp.empty() || nums[i] % temp.back() == 0) {
                    temp.push_back(nums[i]); // Pick
                    solve(nums, temp, i + 1);
                    temp.pop_back(); // Backtrack
                }
                // else: skip (Not pick case is handled implicitly by not picking)
            }
        }
        vector<int> largestDivisibleSubset(vector<int>& nums) {
            sort(nums.begin(), nums.end()); 
            vector<int> temp;
            solve(nums, temp, 0);
            return bestSubset;
        }
    };

 
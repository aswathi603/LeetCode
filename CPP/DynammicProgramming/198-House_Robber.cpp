// https://leetcode.com/problems/house-robber/description/
/*
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


// class Solution {
// public:
//     int rob(vector<int>& nums) {
//         //Recursion 
//        int n= nums.size();
//        return rob(n-1,nums);
//     }

//     int rob(int i, vector<int> & nums){
//         if( i<0) return 0;
//         if( i==0) return nums[0];

//         //steal
//         int pick = nums[i] + rob(i-2,nums);
//         //Skip
//         int skip = rob(i-1,nums);

//         return max(pick,skip);
//     }
// };

//Memoization : TC -O(N) SC- O(N)+O(N)
// class Solution {
// public:
//     int rob(vector<int>& nums) {
//         int n = nums.size();
//         vector<int> dp(n, -1);
//         return rob(n - 1, nums, dp);
//     }

//     int rob(int index, vector<int>& nums, vector<int>& dp) {
//         // Base Cases
//         if(index < 0) return 0;
//         if(index == 0) return nums[0];

//         // Step 2: Memoization check
//         if(dp[index] != -1) return dp[index];

//         // Step 3: Pick or skip the current house
//         int pick = nums[index] + rob(index - 2, nums, dp);
//         int skip = rob(index - 1, nums, dp);

//         return dp[index] = max(pick, skip);
//     }
// };


// Tabulization  TC - O(N)  SC - O(N)
// dp[i] means max money stole till the ith house 
class Solution {
public:
    int rob(vector<int>& nums) {

       int n= nums.size();
       vector<int> dp(n);

        // Base cases
        if(n == 0) return 0;
        if(n == 1) return nums[0];


        dp[0]=nums[0];
        dp[1] = max( nums[0],nums[1]);

        //Iterate in and store it 
        for(int i = 2; i < n; i++) {
            int pick = nums[i] + dp[i - 2];
            int skip = dp[i - 1];
            dp[i] = max(pick, skip);
        }
        return dp[n-1];

    }
};


int main() {
    Solution sol;
    vector<int> nums;
    int n;

    cout << "Enter number of houses: ";
    cin >> n;

    cout << "Enter amount of money in each house:\n";
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        nums.push_back(val);
    }

    int result = sol.rob(nums);
    cout << "Maximum amount that can be robbed: " << result << endl;

    return 0;
}

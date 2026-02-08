// https://leetcode.com/problems/climbing-stairs/description/
/*
70. Climbing Stairs
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
*/

// class Solution {
// public:
//     int climbStairs(int n) {
            // Memoiazation
//         // Step 1 : Initalizaing the dp with -1
//         // vector<int> dp (n+1,-1); Memoization 

            // Tabulization
//         // Step 1 : Initalizaing the dp 
//         vector<int> dp (n+1);
//         return climbStairs(n,dp);

            //Brute Force using recursion
//         // if(n == 1 ||  n==2 ){
//         //     return 1;
//         // }
//         // return climbStairs(n-1)+ climbStairs(n-2);
//     }
        //T.C - O(n)  and  S.C - O(n)+O(n)
//     // //Memoization
//     // int climbStairs(int n,vector<int> &dp) {
//     //     if(n == 1 ||  n==2 ){
//     //         return 1;
//     //     }
//     //     //Step 2 : check the dp before computitng 
//     //     if(dp[n]!=-1) return dp[n];

//     //     //Step 3: Before returning value store it in dp 
//     //     return dp[n] = climbStairs(n-1,dp)+climbStairs(n-2,dp); 
//     // }

//     // //Tabulization   -T.C O(n) and S.C O(n)
//     // int climbStairs(int n,vector<int> &dp) {
//     //     if(n == 1 ||  n==2 ){
//     //         return 1;
//     //     }
//     //     // step 2: intizalizing the base index with the value it has 
//     //     dp[0] = 1;
//     //     dp[1] = 1;
//     //     //Step 3: Iteratinfg for ele till (n+1) --> dp.size();
//     //     for( int i=2;i<n+1;i++){
//     //         dp[i] = dp[i-1]+dp[i-2];
//     //     }
//     //     // return the dp[dp.size()-1];
//     //     return dp[n];
//     // }
//     }
// };



//Extra Space Removal || Sapce Optimization problem 
#include <iostream>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        int prev1 = 1;  // dp[i - 1]
        int prev2 = 1;  // dp[i - 2]

        for (int i = 2; i <= n; ++i) {
            int dp = prev1 + prev2;
            prev2 = prev1;
            prev1 = dp;
        }

        return prev1;
    }
};

int main() {
    Solution sol;
    int n;

    cout << "Enter number of stairs: ";
    cin >> n;

    int ways = sol.climbStairs(n);
    cout << "Number of ways to climb " << n << " stairs: " << ways << endl;

    return 0;
}


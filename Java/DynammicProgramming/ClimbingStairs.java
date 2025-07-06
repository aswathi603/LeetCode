package Java.DynammicProgramming;

// # https://leetcode.com/problems/climbing-stairs/description/

// 70. Climbing Stairs
// Solved
// Easy
// Topics
// premium lock icon
// Companies
// Hint
// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps
// Example 2:

// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step
 

// Constraints:

// 1 <= n <= 45

public class ClimbingStairs {

    // 1. Recursion (Brute Force - TLE for large n)
    public int climbStairsRecursion(int n) {
        if (n <= 2) return n;
        return climbStairsRecursion(n - 1) + climbStairsRecursion(n - 2);
    }

    // // 2. Memoization (Top-down DP)
    // public int climbStairsMemo(int n) {
    //     int[] dp = new int[n + 1];
    //     Arrays.fill(dp, -1);
    //     return memoHelper(n, dp);
    // }

    // // 3. Tabulation (Bottom-up DP)
    // public int climbStairsTab(int n) {
    //     if (n <= 2) return n;

    //     int[] dp = new int[n + 1];
    //     dp[1] = 1;
    //     dp[2] = 2;

    //     for (int i = 3; i <= n; i++) {
    //         dp[i] = dp[i - 1] + dp[i - 2];
    //     }

    //     return dp[n];
    // }

    // // 4. Space Optimization
    // public int climbStairs(int n) {
    //     if (n <= 2) return n;

    //     int prev2 = 1;
    //     int prev1 = 2;

    //     for (int i = 3; i <= n; i++) {
    //         int curr = prev1 + prev2;
    //         prev2 = prev1;
    //         prev1 = curr;
    //     }

    //     return prev1;
    // }

    // @Override
    // public String toString() {
    //     return "ClimbingStairs []";
    // }

    // private int memoHelper(int n, int[] dp) {
    //     if (n <= 2) return n;
    //     if (dp[n] != -1) return dp[n];
    //     dp[n] = memoHelper(n - 1, dp) + memoHelper(n - 2, dp);
    //     return dp[n];
    // }
}

# https://leetcode.com/problems/climbing-stairs/description/

# 70. Climbing Stairs
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45



class Solution:
    # 1. Recursion (TLE for large n)
    def climbStairsRecursion(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairsRecursion(n - 1) + self.climbStairsRecursion(n - 2)

    # 2. Memoization (Top-down DP)
    def climbStairsMemo(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self._helper(n, dp)

    def _helper(self, n: int, dp: list) -> int:
        if n <= 2:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self._helper(n - 1, dp) + self._helper(n - 2, dp)
        return dp[n]

    # 3. Tabulation (Bottom-up DP)
    def climbStairsTab(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # 4. Space Optimization
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev1, prev2 = 2, 1
        for _ in range(3, n + 1):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1

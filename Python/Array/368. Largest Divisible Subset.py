# // 368. Largest Divisible Subset
# // Medium

# // Given a set of distinct positive integers nums, 
# // return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# // answer[i] % answer[j] == 0, or
# // answer[j] % answer[i] == 0
# // If there are multiple solutions, return any of them.

 

# // Example 1:

# // Input: nums = [1,2,3]
# // Output: [1,2]
# // Explanation: [1,3] is also accepted.
# // Example 2:

# // Input: nums = [1,2,4,8]
# // Output: [1,2,4,8]
 

# // Constraints:

# // 1 <= nums.length <= 1000
# // 1 <= nums[i] <= 2 * 109
# // All the integers in nums are unique.

def largestDivisibleSubset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)
    dp = [1] * n  # dp[i] stores length of largest subset ending at nums[i]
    prev = [-1] * n  # prev[i] to track the path
    max_idx = 0

    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > dp[max_idx]:
            max_idx = i

    # Reconstruct the subset
    result = []
    while max_idx != -1:
        result.append(nums[max_idx])
        max_idx = prev[max_idx]

    return result[::-1] 
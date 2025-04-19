# 2563. Count the Number of Fair Pairs
# Solved
# Medium

# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:

# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
 

# Example 1:

# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:

# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
 

# Constraints:

# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109

import bisect

def countFairPairs(nums, lower, upper):
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n):
        left = bisect.bisect_left(nums, lower - nums[i], i + 1)
        right = bisect.bisect_right(nums, upper - nums[i], i + 1)
        count += right - left

    return count

# Example usage
nums1 = [0, 1, 7, 4, 4, 5]
lower1, upper1 = 3, 6
print(countFairPairs(nums1, lower1, upper1))  # Output: 6

nums2 = [1, 7, 9, 2, 5]
lower2, upper2 = 11, 11
print(countFairPairs(nums2, lower2, upper2))  # Output: 1

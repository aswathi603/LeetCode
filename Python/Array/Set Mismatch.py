'''
Question Link: https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
Q1. Set Mismatch
Solved
Easy
Topics
premium lock icon
Companies
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
676,400/1.5M
Acceptance Rate
44.3%
Topics
icon
Companies
Similar Questions


'''

from ast import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(nums)
        duplicate = sum(nums) - sum(s)
        missing = sum(range(1, n + 1)) - sum(s)
        return [duplicate, missing]
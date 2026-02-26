'''

Question Link : https://leetcode.com/problems/remove-duplicate-letters/description/

316. Remove Duplicate Letters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

'''

from typing import List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)      # count of remaining characters
        stack = []
        visited = set()
        
        for ch in s:
            freq[ch] -= 1     # character is being used
            
            if ch in visited:
                continue
            
            # maintain lexicographical order
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                visited.remove(stack.pop())
            
            stack.append(ch)
            visited.add(ch)
        
        return "".join(stack)  
'''
Question Link : https://leetcode.com/problems/reverse-nodes-in-k-group/description/

686. Repeated String Match
Medium
Topics
premium lock icon
Companies
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2:

Input: a = "a", b = "aa"
Output: 2
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist of lowercase English letters.

'''

# Solution 1: Brute Force
# time complexity: O(n^2)
# space complexity: O(n)

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        
        while len(repeated) < len(b):
            repeated += a
            count += 1
            
        if b in repeated:
            return count
        elif b in repeated + a:
            return count + 1
        else:
            return -1
        

# Solution 2: KMP Algorithm
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def kmp(pattern):
            lps = [0] * len(pattern)
            j = 0
            
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            
            return lps
        
        lps = kmp(b)
        i = j = 0
        count = 1
        
        while i < len(a) * (len(b) // len(a) + 2):
            if a[i % len(a)] == b[j]:
                i += 1
                j += 1
                if j == len(b):
                    return count
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
            
            if i % len(a) == 0:
                count += 1
        
        return -1
    

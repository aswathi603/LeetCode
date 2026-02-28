'''
Question Link:  https://www.geeksforgeeks.org/print-all-permutations-of-a-given-string-using-backtracking/

Permutations of a String
Difficulty: MediumAccuracy: 34.65%Submissions: 337K+Points: 4
Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

Examples:

Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.
Input: s = "ABSG"
Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
Explanation: Given string ABSG has 24 unique permutations.
Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.
Constraints:
1 <= s.size() <= 9
s contains only Uppercase english alphabets

Expected Complexities
Time Complexity: O(log n)
Auxiliary Space: O(log n)


'''

#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        s = sorted(s)
        n = len(s)
        visited = [False] * n
        result = []

        def backtrack(path):
            if len(path) == n:
                result.append("".join(path))
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                
                # Skip duplicates
                if i > 0 and s[i] == s[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                path.append(s[i])
                backtrack(path)
                path.pop()
                visited[i] = False
        
        backtrack([])
        return result    

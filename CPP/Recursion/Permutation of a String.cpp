/*
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

*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<string> findPermutation(string &s) {
        // Code here there
        vector<string> ans;
        sort(s.begin(), s.end());
        do {
            ans.push_back(s);
        } while (next_permutation(s.begin(), s.end()));
        return ans;

    }
};

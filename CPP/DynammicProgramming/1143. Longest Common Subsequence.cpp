// 1143. Longest Common Subsequence
// Solved
// Medium

// Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".
// A common subsequence of two strings is a subsequence that is common to both strings.

 

// Example 1:

// Input: text1 = "abcde", text2 = "ace" 
// Output: 3  
// Explanation: The longest common subsequence is "ace" and its length is 3.
// Example 2:

// Input: text1 = "abc", text2 = "abc"
// Output: 3
// Explanation: The longest common subsequence is "abc" and its length is 3.
// Example 3:

// Input: text1 = "abc", text2 = "def"
// Output: 0
// Explanation: There is no such common subsequence, so the result is 0.
 

// Constraints:

// 1 <= text1.length, text2.length <= 1000
// text1 and text2 consist of only lowercase English characters.

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size(), m = text2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (text1[i-1] == text2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
    }
};

int main() {
    Solution sol;
    cout << sol.longestCommonSubsequence("abcde", "ace") << endl;   // 3
    cout << sol.longestCommonSubsequence("abc", "abc") << endl;     // 3
    cout << sol.longestCommonSubsequence("abc", "def") << endl;     // 0
    return 0;
}



    
    
    // // Tabulization  for another way 
    // int longestCommonSubsequence(string text1, string text2) {
    //int n=text1.size(),m=text2.size();
    
    //vector<vector<int>> dp(n+1,vector<int>(m+1,0));
    
    // for (int i = n - 1; i >= 0; --i) {
    //             for (int j = m - 1; j >= 0; --j) {
    //                 if (s1[i] == s2[j]) {
    //                     dp[i][j] = 1 + dp[i + 1][j + 1];
    //                 } else {
    //                     dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]);
    //                 }
    //             }
    //         }
    
    //         return dp[0][0];
    //     }
    // };
    
    
    //Memoization Method 
    // int longestCommonSubsequence(string text1, string text2) {
    //         int n=text1.size() ,m=text2.size();
    //         vector<vector<int>> dp(n,vector<int>(m,-1));
    //         return LCS(0,0,text1,text2,dp);
    //     }
    //     int LCS(int i,int j,string &s1,string &s2,vector<vector<int>> &dp){
    //         if(i>=s1.size() ||j>=s2.size()) return 0;
    
    //         if(dp[i][j]!=-1){
    //             return dp[i][j];
    //         }
    //         if(s1[i]==s2[i]){
    //             return dp[i][j]= 1+ LCS(i+1,j+1,s1,s2,dp);
    //         }else{
    //             return dp[i][j]=max(LCS(i+1,j,s1,s2,dp),LCS(i,j+1,s1,s2,dp));
    //         }
    
    //     }
    // };
    
    
    // Recursion Method 
    
    // int longestCommonSubsequence(string text1, string text2) {
    //         return LCS(0,0,text1,text2);
    //     }
    //     int LCS(int i, int j,string s1,string s2){
    //         if(i>s1.size() || i>=s2.size()){
    //             return 0;
    //         }
    //         if(s1.at(i)==s2.at(i)){
    //             return 1+LCS(i+1,j+1,s1,s2);
    //         }else{
    //             return max(LCS(i,j+1,s1,s2),LCS(i+1,j,s1,s2));
    //         }
    //     }
    // };
// <!-- https://leetcode.com/problems/fair-distribution-of-cookies/description -->

// 2305. Fair Distribution of Cookies
// Solved
// Medium
// Topics
// premium lock icon
// Companies
// Hint
// You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

// The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

// Return the minimum unfairness of all distributions.

 

// Example 1:

// Input: cookies = [8,15,10,20,8], k = 2
// Output: 31
// Explanation: One optimal distribution is [8,15,8] and [10,20]
// - The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
// - The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
// The unfairness of the distribution is max(31,30) = 31.
// It can be shown that there is no distribution with an unfairness less than 31.
// Example 2:

// Input: cookies = [6,1,3,2,2,4,1,2], k = 3
// Output: 7
// Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
// - The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
// - The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
// - The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
// The unfairness of the distribution is max(7,7,7) = 7.
// It can be shown that there is no distribution with an unfairness less than 7.
 

// Constraints:

// 2 <= cookies.length <= 8
// 1 <= cookies[i] <= 105
// 2 <= k <= cookies.length

// Approach
// You want to assign each cookie to one of the k children.

// You use backtracking to try all possible distributions.

// For every complete distribution (i.e., all cookies are assigned):

// Find out how many cookies each child got.

// Take the maximum among them.

// Try to minimize that value across all valid assignments.

// Keep track of the best (smallest) such maximum using a global minimum (Ans in your C++ code).



#include<bits./stdc++.h>
#include<vector>
using namespace std;

class Solution {
public:
    int Ans =INT_MAX;
    void maxTotalCookies(vector<int> & cookies,int k,int index,vector<int> &children){
        if( index == cookies.size()){
            int maxRes=INT_MIN;
            for( int val: children){
                maxRes=max(maxRes,val);
            }
            Ans = min(Ans,maxRes);
            return;
        }
        for( int i =0;i<k;i++){
            int cookie =cookies[index];
            children[i]+=cookie;
            maxTotalCookies(cookies,k,index+1,children);
            children[i]-=cookie;
        }
    }
    int distributeCookies(vector<int>& cookies, int k) {
        vector<int> children(k);
        maxTotalCookies(cookies,k,0,children);
        return Ans;
    }
};
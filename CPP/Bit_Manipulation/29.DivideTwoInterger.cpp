/*
29. Divide Two Integers
Solved
Medium
Topics
premium lock icon
Companies
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
*/
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int divide(int dividend, int divisor) {
        int MaxInt = INT_MAX;
        int MinInt = INT_MIN;

        if (dividend == MinInt && divisor ==-1) return MaxInt;
        if (dividend == MinInt && divisor ==1) return MinInt;

        if (dividend == 0) return 0;

        if (divisor == 1) return dividend;
        if(divisor == -1) return -dividend;

        int sign  = (dividend > 0 ) ^ (divisor > 0) ? -1 : 1;
        long long dvd = labs(dividend);
        long long dvs = labs(divisor);
        int quotient = 0;

        while( dvd >= dvs){
            long long temp =dvs, multiple = 1;
            while (dvd > (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            quotient += multiple;
        }
        long long result = sign * quotient;
        return result > MaxInt ? MaxInt : result < MinInt ? MinInt : result;
    }
};

/*
191. Number of 1 Bits
Solved
Easy
Topics
premium lock icon
Companies
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?

*/

# include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count += (n & 1);   // Check the last bit
            n >>= 1;           // Shift right to check the next bit
        }
        return count;
    }
};


// Optimised Approach:
class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);  // Drops the lowest set bit
            count++;
        }
        return count;
    }
};

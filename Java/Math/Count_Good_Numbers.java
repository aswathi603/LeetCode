package Java.Math;

// 1922. Count Good Numbers
// Solved
// Medium

// A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

// For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
// Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

// A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

// Example 1:

// Input: n = 1
// Output: 5
// Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
// Example 2:

// Input: n = 4
// Output: 400
// Example 3:

// Input: n = 50
// Output: 564908303
 

// Constraints:

// 1 <= n <= 1015
import java.util.Scanner;


class Solution {
        private static final int MOD = 1_000_000_007;

        // Fast Modular Exponentiation
        private long modPow(long base, long exp) {
            long result = 1;
            base %= MOD;

            while (exp > 0) {
                if ((exp & 1) == 1) {
                    result = (result * base) % MOD;
                }
                base = (base * base) % MOD;
                exp >>= 1;
            }

            return result;
        }

        public int countGoodNumbers(final long n) {
            final long evenPositions = (n + 1) / 2;
            final long oddPositions = n / 2;

            final long evenWays = modPow(5, evenPositions);
            final long oddWays = modPow(4, oddPositions);

            return (int)((evenWays * oddWays) % MOD);
        }
    public static void main(final String[] args) {
        @SuppressWarnings("resource")
        final Scanner scanner = new Scanner(System.in);
        final Solution sol = new Solution();

        System.out.print("Enter length of digit string (n): ");
        final long n = scanner.nextLong();

        final int result = sol.countGoodNumbers(n);
        System.out.println("Total number of good digit strings of length " + n + " is: " + result);
    }
}



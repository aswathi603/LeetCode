// 118. Pascal's Triangle

// Description:
// Given an integer numRows, return the first numRows of Pascal's triangle.
// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

// Example 1:
// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

// Example 2:
// Input: numRows = 1
// Output: [[1]]
 

// Constraints:
// 1 <= numRows <= 30


import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> tri = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            for (int k = 0; k < i + 1; k++){
                row.add(1);
            }

            if (i > 0) {
                for (int j = 1; j < i; j++) {
                    row.set(j, tri.get(i - 1).get(j - 1) + tri.get(i - 1).get(j));
                }
            }

            tri.add(row);
        }
        return tri;
    }
}

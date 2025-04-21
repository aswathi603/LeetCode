// 781. Rabbits in Forest
// Medium

// There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

// Given the array answers, return the minimum number of rabbits that could be in the forest.

 

// Example 1:

// Input: answers = [1,1,2]
// Output: 5
// Explanation:
// The two rabbits that answered "1" could both be the same color, say red.
// The rabbit that answered "2" can't be red or the answers would be inconsistent.
// Say the rabbit that answered "2" was blue.
// Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
// The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
// Example 2:

// Input: answers = [10,10,10]
// Output: 11
 

// Constraints:

// 1 <= answers.length <= 1000
// 0 <= answers[i] < 1000


import java.util.*;

public class RabbitsInForest {
    public static int numRabbits(int[] answers) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int a : answers) count.put(a, count.getOrDefault(a, 0) + 1);

        int res = 0;
        for (int x : count.keySet()) {
            int groupSize = x + 1;
            int groups = (int) Math.ceil((double) count.get(x) / groupSize);
            res += groups * groupSize;
        }
        return res;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter number of elements: ");
            int n = sc.nextInt();
            int[] answers = new int[n];
            System.out.println("Enter the answers array:");
            for (int i = 0; i < n; i++) {
                answers[i] = sc.nextInt();
            }

            System.out.println("Minimum number of rabbits in the forest: " + numRabbits(answers));
        }
    }
}

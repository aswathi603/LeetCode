import java.util.*;

public class LargestDivisibleSubset {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        if (nums.length == 0) return new ArrayList<>();

        Arrays.sort(nums);
        int n = nums.length;
        int[] dp = new int[n]; // length of largest subset ending at i
        int[] prev = new int[n]; // backtrack path
        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);

        int maxIndex = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > dp[maxIndex]) {
                maxIndex = i;
            }
        }

        List<Integer> result = new ArrayList<>();
        while (maxIndex != -1) {
            result.add(nums[maxIndex]);
            maxIndex = prev[maxIndex];
        }
        Collections.reverse(result);
        return result;
    }
}



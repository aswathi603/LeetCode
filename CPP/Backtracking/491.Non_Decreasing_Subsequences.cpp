#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void backtrack(int index, vector<int>& nums, vector<int>& path, set<vector<int>>& res) {
        if (path.size() >= 2) {
            res.insert(path);  // Store valid subsequence
        }
        if (index == nums.size()) return;

        // Pick the current element if it's non-decreasing
        if (path.empty() || nums[index] >= path.back()) {
            path.push_back(nums[index]);
            backtrack(index + 1, nums, path, res);
            path.pop_back();  // Backtrack
        }

        // Non-Pick (Skip the current element)
        backtrack(index + 1, nums, path, res);
    }

    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> res;  // Use a set to store unique subsequences
        vector<int> path;
        backtrack(0, nums, path, res);

        return vector<vector<int>>(res.begin(), res.end());  // Convert set to vector
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {4, 6, 7, 7};
    vector<int> nums2 = {4, 4, 3, 2, 1};

    vector<vector<int>> res1 = sol.findSubsequences(nums1);
    vector<vector<int>> res2 = sol.findSubsequences(nums2);

    for (auto& seq : res1) {
        cout << "[";
        for (int num : seq) cout << num << " ";
        cout << "] ";
    }
    cout << endl;

    for (auto& seq : res2) {
        cout << "[";
        for (int num : seq) cout << num << " ";
        cout << "] ";
    }
    cout << endl;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void backtrack(int index, vector<int>& nums, vector<int>& path, set<vector<int>>& res) {
        if (path.size() >= 2) {
            res.insert(path);  // Store valid subsequence
        }
        if (index == nums.size()) return;

        // Pick the current element if it's non-decreasing
        if (path.empty() || nums[index] >= path.back()) {
            path.push_back(nums[index]);
            backtrack(index + 1, nums, path, res);
            path.pop_back();  // Backtrack
        }

        // Non-Pick (Skip the current element)
        backtrack(index + 1, nums, path, res);
    }

    vector<vector<int>> findSubsequences(vector<int>& nums) {
        set<vector<int>> res;  // Use a set to store unique subsequences
        vector<int> path;
        backtrack(0, nums, path, res);

        return vector<vector<int>>(res.begin(), res.end());  // Convert set to vector
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {4, 6, 7, 7};
    vector<int> nums2 = {4, 4, 3, 2, 1};

    vector<vector<int>> res1 = sol.findSubsequences(nums1);
    vector<vector<int>> res2 = sol.findSubsequences(nums2);

    for (auto& seq : res1) {
        cout << "[";
        for (int num : seq) cout << num << " ";
        cout << "] ";
    }
    cout << endl;

    for (auto& seq : res2) {
        cout << "[";
        for (int num : seq) cout << num << " ";
        cout << "] ";
    }
    cout << endl;

    return 0;
}

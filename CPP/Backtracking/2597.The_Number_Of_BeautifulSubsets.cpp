#include <bits/stdc++.h>;
using namespace std;
class Solution {
    private:
        bool isBeautiful(vector<int>& subsets,int k){
            for(int i=0;i<subsets.size();++i){
                for(int j=i+1;j<subsets.size();++j){
                    if(abs(subsets[i]-subsets[j])==k){
                        return false;
                    }
                }
            }
            return true;
        }
    
        void solve(vector<int>& nums,int k,int index,vector<int>& subsets,int& count){
            //Base Case
            if(index==nums.size()){
                if(!subsets.empty() && isBeautiful(subsets,k)){
                    count++;
                }
                return ;
            }
    
            //Not Picked
            solve(nums,k,index+1,subsets,count);
    
            //Picked the subset means include
            subsets.push_back(nums[index]);
            solve(nums,k,index+1,subsets,count);
    
            //Backtrack
            subsets.pop_back();
        }
    public:
        int beautifulSubsets(vector<int>& nums, int k) {
            int count=0;
            vector<int> subsets;
            solve(nums,k,0,subsets,count);
            return count;
        }
};
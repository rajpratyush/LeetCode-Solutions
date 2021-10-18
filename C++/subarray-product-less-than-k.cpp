class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        
        if (k <= 1 || nums.size() == 0) return 0;
        
        int res = 0, i = 0, j = 0, prod = 1;
        
        for (i = 0; i < nums.size(); i++) {
            prod *= nums[i];
            
            while(j < nums.size() && prod >= k) {
                prod /= nums[j];
                j++;
            }
            
            res += i-j+1;
        }
        
        return res;
    }
};
// Time:  O(n)
// Space: O(k)

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> dq;
        for (int i = 0; i < nums.size(); ++i) {
            if (i >= k && !dq.empty() && i - dq.front() == k) {
                dq.pop_front();
            }
            while (!dq.empty() && nums[i] >= nums[dq.back()]) {
                dq.pop_back();
            }
            dq.emplace_back(i);
            if (i >= k - 1) {
                result.emplace_back(nums[dq.front()]);
            }
        }
        return result;
    }
};

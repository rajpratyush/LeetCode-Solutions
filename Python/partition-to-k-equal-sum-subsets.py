

# Time:  O(k^(n-k) * k!)
# Space: O(n)
# DFS solution with pruning.
class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums, target, i, subset_sums):
            if i == len(nums):
                return True
            for k in xrange(len(subset_sums)):
                if subset_sums[k]+nums[i] > target:
                    continue
                subset_sums[k] += nums[i]
                if dfs(nums, target, i+1, subset_sums):
                    return True
                subset_sums[k] -= nums[i]
                if not subset_sums[k]: break
            return False

        total = sum(nums)
        if total%k != 0 or max(nums) > total//k:
            return False
        nums.sort(reverse=True)
        subset_sums = [0] * k
        return dfs(nums, total//k, 0, subset_sums)


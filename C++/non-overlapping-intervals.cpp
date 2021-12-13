// Time:  O(nlogn)
// Space: O(1)

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

	if (intervals.empty()) return 0;

	sort(intervals.begin(), intervals.end());
	int cnt = -1;
	int prev = INT_MAX;
	for (vector<int>& interval : intervals) {
		if (interval[0] < prev) {
			++cnt;
			prev = min(prev, interval[1]);
			continue;
		}
		prev = interval[1];
	}
	return cnt;
}
};

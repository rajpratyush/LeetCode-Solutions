# Time:  O(nlogn)
# Space: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        
        intervals.sort()
        rms = 0
        pre_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < pre_end:
                rms += 1
                pre_end = min(end, pre_end)
            else:
                pre_end = end
        return rms


from bisect import *
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n=len(matrix), len(matrix[0])
        for j in range(n):
            for i in range(1, m):
                matrix[i][j]=matrix[i-1][j]+matrix[i][j]
        res=float('-inf') # k could be smaller than 0
        for l in range(n):
            prefix = [0]*(m)
            for r in range(l, n):
                for i in range(m):
                    prefix[i]+=matrix[i][r]
                sorted_ = [0]  # we can always select all front numbers.
                for pre in prefix:
                    pos = bisect_left(sorted_, pre-k)
                    if pos < len(sorted_):
                        res=max(res, pre-sorted_[pos])
                    insort(sorted_, pre)
        return res
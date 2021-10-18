from collections import defaultdict
from decimal import getcontext, Decimal
getcontext().prec = 25
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def getLine(pt1, pt2):
            x1, y1 = pt1
            x2, y2 = pt2
                
            m = Decimal(y2-y1)/Decimal(x2-x1) if x1 != x2 else float('inf')
            c = y1 - m * x1 if x1 != x2 else x1
            
            return m, c
        
        # points.sort()
        n = len(points)

        if n < 3:
            return n
        
        curmax = 0
        
        # line represented as gradient, y intercept
        for i, pt1 in enumerate(points[:-1]):
            lines_i = defaultdict(int)
            duplicate = 0
            maxlines = 0
            for pt2 in points[(i+1):]:
                if pt2 == pt1:
                    duplicate += 1
                    continue
                line = getLine(pt1, pt2)
                lines_i[line] += 1
                maxlines = max(maxlines, lines_i[line])
            curmax = max(curmax, maxlines + duplicate + 1)
                
        return curmax
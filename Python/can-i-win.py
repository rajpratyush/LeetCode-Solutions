class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal<=maxChoosableInteger:
            return True
        if (maxChoosableInteger+1)*maxChoosableInteger//2<desiredTotal:
            return False
        
        def dfs(mask,dp,maxChoosableInteger,desiredTotal):
            if desiredTotal in dp and mask in dp[desiredTotal]:
                return dp[desiredTotal][mask]
            if desiredTotal not in dp:
                dp[desiredTotal]={}
            dp[desiredTotal][mask]=True
            for i in range(maxChoosableInteger,0,-1):
                t=1<<i
                if (mask&t)==0:
                    mask|=t
                    if i>=desiredTotal or not dfs(mask,dp,maxChoosableInteger,desiredTotal-i):
                        dp[desiredTotal][mask]=True
                        return True
                    mask^=t
            dp[desiredTotal][mask]=False
            return False
            
        return dfs(0,dict(),maxChoosableInteger,desiredTotal)
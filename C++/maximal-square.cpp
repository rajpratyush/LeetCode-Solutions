class Solution {
public:
    inline int min(int x, int y) {
        return x<y? x:y;
    }
    inline int min(int x, int y, int z) {
        return min(x, min(y, z));
    }
    int maximalSquare(vector<vector<char>>& matrix) {
        int row = matrix.size();
        if (row <=0) return 0;
        int col = matrix[0].size();
        
        int maxSize = 0;
        vector<vector<int>> dp(row, vector<int>(col));
        
        for (int i=0; i<matrix.size(); i++) {
            for (int j=0; j<matrix[i].size(); j++){
                //convert the `char` to `int`
                dp[i][j] = matrix[i][j] -'0';
                //for the first row and first column, or matrix[i][j], dp[i][j] is ZERO
                //so, it's done during the previous conversion
                
                // i>0 && j>0 && matrix[i][j]=='1'
                if (i!=0 && j!=0 & dp[i][j]!=0){
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
                }
                
                //tracking the maxSize
                if (dp[i][j] > maxSize ){
                    maxSize = dp[i][j];
                }
            }
        }
        
        return maxSize*maxSize;
    }
};

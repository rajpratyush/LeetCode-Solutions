class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        if(n < 2) return n;
        vector<vector<int>> dp(n, vector<int>(n, 2));
        //dp[i][j] max number of points on the line of pint i and j
        
        int max = 2;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(j == i || dp[i][j] != 2) continue;
                vector<int> p1 = points[i];
                vector<int> p2 = points[j];
                vector<int> currSet = {i, j};
                for(int k = 0; k < n; k++)
                {
                    if(k == i || k == j) continue;
                    vector<int> p3 = points[k];
                    //if one the same line, push the point to the point set
                    if(((long)p3[0]-(long)p2[0])*((long)p2[1]-(long)p1[1]) 
                       == ((long)p2[0]-(long)p1[0])*((long)p3[1]-(long)p2[1]))
                        currSet.push_back(k);
                }
                //set all combinations to the size of the set
                if(currSet.size()!=2)
                {
                    for(int m = 0; m < currSet.size(); m++)
                    {
                         for(int n = 0; n < currSet.size(); n++)
                         {
                             if(m!=n) dp[currSet[m]][currSet[n]] = currSet.size();
                         }
                    }
                }
                max = std::max(max, (int)currSet.size());
            }
        }
        return max;
    }
};
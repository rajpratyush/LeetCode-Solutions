// Time:  O(n)
// Space: O(1)

Idea:
Iterate through the intervals array checking

If newinter's end is less than current interval's start, if so add the new interval and break.
Elseif newinter's start is greater that current interval's end , add curr interval and continue.
Else there is overlap. Store Min start. Iterate till you find a start that is less that new inter end.
Cur inter------/////////--/////////------///////////-----////////
New ------------ //////////////////////////////
--------------ms----------------------------me
ms = min start , me = max end
After the loop is done check if all intervals are inserted and add the remaining.
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& inters, vector<int>& newinter) {
        vector<vector<int>> finale;
        int i,j=0;
        for(i=0;i<inters.size();i++){
            if(newinter[1]<inters[i][0]){
                finale.push_back(newinter);
                j=1;
                break;
            }
            else if(newinter[0]>inters[i][1]){
                finale.push_back(inters[i]);
            }
            else{
                int min_start = min(newinter[0],inters[i][0]);
                while(i+1<inters.size() && newinter[1]>=inters[i+1][0]) i++;                
                int max_end = max(newinter[1],inters[i][1]);
                finale.push_back({min_start,max_end});
                j=1;
                i++;
                break;
            }
        }
        if(j){
            while(i<inters.size()) finale.push_back(inters[i++]);
        }
        else{
            finale.push_back(newinter);
        }
        
        return finale;
    }
};

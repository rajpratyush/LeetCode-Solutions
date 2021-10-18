class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        def binarySearch(idx,right_el,arr,arr1):
            
            lo = 0
            hi = len(arr)-1
            index = -1
            curr_min = float('inf')
            
            while (lo <= hi):
                mid = (lo+hi)//2
                left_el = arr[mid]
                if(right_el <= left_el and arr1[mid][0] != idx):
                    if(left_el - right_el <= curr_min):
                        curr_min = left_el - right_el
                        index = arr1[mid][0]
                        hi = mid-1
                        
                else:
                    lo = mid + 1
                    
            return index
                    
        
        dict_first = {}
        dict_sec = {}

        for idx,(fr,se) in enumerate(intervals):
            dict_first[idx] = fr
            dict_sec[idx] = se
            
            
        arr1= list(sorted(dict_first.items(),key = lambda x:x[1],reverse=False))
        
        fr_list = []
        res = []
        
        for el in arr1:
            fr_list.append(el[1])
            
        for k,v in dict_sec.items():
            res.append(binarySearch(k,v,fr_list,arr1))
            
        return res
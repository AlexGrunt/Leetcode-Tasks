class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        i = 0
        
        while i < len(intervals):
            curr_interval = intervals[i].copy()
            
            while i + 1 < len(intervals) and intervals[i + 1][0] <= curr_interval[1]:
                curr_interval[1] = max(curr_interval[1], intervals[i + 1][1])
                i = i + 1
            result.append(curr_interval)
            i = i + 1
            
        return result
            
                
                
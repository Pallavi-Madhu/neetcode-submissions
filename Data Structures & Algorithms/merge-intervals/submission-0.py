class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #start = [x for x in ]
        #intervals.sort(key = lambda x : x.start)
        # res = []
        # for i in range(len(intervals) - 1):
        #     if intervals[i][1] <= intervals[i+1][0]:
        #         res.append([intervals[i][0],intervals[i+1][1]])
        # return res
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        for current in intervals[1:]:
            last_added = res[-1]
            if current[0] <= last_added[1]:
                last_added[1] = max(last_added[1],current[1])
            else:
                res.append(current)
        return res
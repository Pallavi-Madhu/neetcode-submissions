class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for i,point in enumerate(points):
            dist = ( (point[0] - 0)**2 + (point[1] - 0)**2 ) 
            result.append((dist , point))
        heapq.heapify(result)

        final= [] 

        while k > 0:
            final.append(heapq.heappop(result)[1])
            k -= 1
        return final

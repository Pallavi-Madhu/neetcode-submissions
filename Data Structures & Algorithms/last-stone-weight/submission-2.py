class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            seco_heavy = -heapq.heappop(stones)

            if heaviest != seco_heavy:
                heapq.heappush(stones,-(heaviest - seco_heavy ))
            else:
                heapq.heappush(stones, 0)
        if stones:
            return  -stones[0]
        else:
            return None

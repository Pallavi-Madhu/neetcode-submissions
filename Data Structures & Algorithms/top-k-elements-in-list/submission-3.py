class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash_map = {}
        # l = []
        # for num in nums:
        #     if num not in hash_map:
        #         hash_map[num ] = 1
        #     else:
        #         hash_map[num] += 1
        # sorted_items = sorted(hash_map.items(),key = lambda x: x[1], reverse = True)
        # l = [num for num , freq in sorted_items[:k]]
        # return l
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1

        heap = []
        for num,freq in hash_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        top_k = [num for (freq,num) in  heap]
        return top_k



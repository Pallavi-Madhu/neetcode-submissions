class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        l = []
        for num in nums:
            if num not in hash_map:
                hash_map[num ] = 1
            else:
                hash_map[num] += 1
        sorted_items = sorted(hash_map.items(),key = lambda x: x[1], reverse = True)
        l = [num for num , freq in sorted_items[:k]]
        return l
        #for i in hash_map :
            #if hash_map[i] >= k:
                #l.append(i)     
        #return list(l)
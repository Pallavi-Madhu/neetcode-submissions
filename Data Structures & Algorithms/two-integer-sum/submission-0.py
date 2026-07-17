class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,num in enumerate(nums):
            req = target - num
            if req not in hash_map:
                hash_map[num] = i
            else:
                return [hash_map[req],i]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        final = []
        while r <= len(nums):
            maxE = max(nums[l:r])
            final.append(maxE)
            l += 1
            r += 1
        return final
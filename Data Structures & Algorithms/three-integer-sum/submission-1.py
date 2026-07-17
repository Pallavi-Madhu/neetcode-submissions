class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        nums_sorted = sorted(nums)
        for i in range(l):
            if i>0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            a = nums_sorted[i]
            left = i+1
            right = l-1
            while (left < right):
                if nums_sorted[left] + nums_sorted[right] + a == 0:
                    res.append([a,nums_sorted[left],nums_sorted[right]])
                    left += 1
                    right -= 1
                    while left<right and nums_sorted[left] == nums_sorted[left-1]:
                        left += 1
                
                elif nums_sorted[left] + nums_sorted[right] + a > 0:
                    right = right - 1
                else:
                    left = left + 1
        return res

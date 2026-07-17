class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # l = len(nums)
        # for i in range(l+1):
        #     if i not in nums:
        #         return i

        n = len(nums)
        expected_sum = (n*(n+1))//2
        calc_sum = sum(nums)
        return expected_sum - calc_sum
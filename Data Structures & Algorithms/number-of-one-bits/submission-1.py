class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        #APPROACH 1
        # while n:
        #     res += n%2
        #     n = n >> 1
        # return res

        #APPROACH 2
        while n:
            n = n&(n-1)
            res += 1
        return res
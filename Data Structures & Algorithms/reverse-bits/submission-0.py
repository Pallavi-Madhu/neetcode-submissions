class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1 #extract last bit
            res = (res << 1) | bit #shift res left one bit and add the but 
            n = n >> 1  #right shift input n 
        return res

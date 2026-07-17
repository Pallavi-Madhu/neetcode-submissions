class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.to_bin(i))
        return res
    
    def to_bin(self,n:int):
        count = 0
        while n:
            r = n % 2
            if r == 1:
                count += 1
            n = n//2
        return count    
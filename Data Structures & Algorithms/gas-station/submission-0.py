class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        res = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i+1
        return res

# gas  = [1, 2, 3, 4, 5]

# cost = [3, 4, 5, 1, 2]

# Global check: sum(gas) = 15, sum(cost) = 15. 15 < 15 is False. A solution exists!

# i = 0: total += (1 - 3) = -2. total < 0 triggers! Reset total = 0, set res = 1.

# i = 1: total += (2 - 4) = -2. total < 0 triggers! Reset total = 0, set res = 2.

# i = 2: total += (3 - 5) = -2. total < 0 triggers! Reset total = 0, set res = 3.

# i = 3: total += (4 - 1) = 3. total is positive. res stays 3.

# i = 4: total += (5 - 2) = 3 + 3 = 6. total is positive. Loop ends.

# The function returns res = 3 (index 3, which corresponds to the gas station with value 4).
        
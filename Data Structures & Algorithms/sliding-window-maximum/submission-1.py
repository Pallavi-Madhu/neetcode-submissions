class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l = 0
        # r = k
        # final = []
        # while r <= len(nums):
        #     maxE = max(nums[l:r])
        #     final.append(maxE)
        #     l += 1
        #     r += 1
        # return final

        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)     #strictly decreasing q

            #remove left val from winfow
            if l > q[0]:
                q.popleft()
            
            #shifting window
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
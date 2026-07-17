class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        #store as height,index
        for i,height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                w = i - j
                area = h*w
                maxArea = max(maxArea,area)
                start = j
            stack.append((height,start))

        #pop remaining
        while stack:
            h,j = stack.pop()
            w = n-j
            area = h*w
            maxArea = max(area,maxArea)
        return maxArea
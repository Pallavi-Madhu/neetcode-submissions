class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,right = 0,len(matrix)-1
        while l < right:
            top,bottom = l,right
            for i in range(right-l):

                #save topleft
                topLeft = matrix[top][l+i]

                #move bottom left to top left
                matrix[top][l+i] = matrix[bottom - i][l]

                #move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][right - i]

                #move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                #move top left to top right
                matrix[top + i][right] = topLeft
            
            l += 1
            right -= 1
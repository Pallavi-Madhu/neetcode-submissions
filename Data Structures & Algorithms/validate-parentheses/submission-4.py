class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = 0
        for char in s:
            if char == "(" or char =="{" or char == "[":
                stack.append(char)
                top += 1
            else:
                if top == 0:
                    return False
                if char == ")" and stack[top-1] == "(":
                    stack.pop()
                    top -= 1
                elif char == "}" and stack[top-1] == "{":
                    stack.pop()
                    top -= 1
                elif char == "]" and stack[top-1] == "[":
                    stack.pop()
                    top -= 1
                else:
                    return False
            
        return top == 0
        
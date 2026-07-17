class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        top = -1
        for num in tokens:
            if num not in ["+","-","*","/"]:
                top += 1
                stack.append(int(num))
            else:
                a = stack.pop()
                top -= 1
                b = stack.pop()
                top -= 1
                if num == "+":
                    res = b+a
                    stack.append(res)
                elif num == "-":
                    res = b-a
                    stack.append(res)
                elif num == "*":
                    res = a*b
                    stack.append(res)
                elif num == "/":
                    stack.append(int(b/a))
                top += 1
                
        return stack.pop()

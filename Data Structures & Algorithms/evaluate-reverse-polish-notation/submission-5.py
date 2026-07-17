class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-/*":
                a = stack.pop()
                b = stack.pop()

                if ch == "+":
                    stack.append(int(b+a))
                elif ch == "-":
                    stack.append(int(b-a))
                elif ch == "*":
                    stack.append(int(a*b))
                elif ch == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(ch))
        return stack[-1]

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack =[]
        for i ,ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()   #match found,then pop its index
                else:
                    s[i] = ''   #match not found ie extrs ),remove it
        for i in stack:
            s[i] = ''           #remove unmatched (
        return ''.join(s)

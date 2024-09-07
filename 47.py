class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif c == "D":
                a = stack[-1]
                b = a * 2
                stack.append(b)
            elif c == "C":
                stack.pop()
            else:
                stack.append(int(c))
        return sum(stack)

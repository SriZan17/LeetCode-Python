class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    r = a + b
                elif token == "-":
                    r = a - b
                elif token == "*":
                    r = a * b
                elif token == "/":
                    r = int(a / b)
                stack.append(str(r))
            else:
                stack.append(str(token))
        return int(stack.pop())

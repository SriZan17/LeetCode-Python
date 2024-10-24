class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # Validate Row
        for i in range(n):
            s = []
            for j in range(n):
                item = matrix[i][j]
                s.append(item)
            for num in range(1, n + 1):
                if num not in s:
                    return False

        # Validate Colums
        for i in range(n):
            s = []
            for j in range(n):
                item = matrix[j][i]
                s.append(item)
            for num in range(1, n + 1):
                if num not in s:
                    return False

        return True

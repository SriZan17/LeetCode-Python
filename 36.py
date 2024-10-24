class Solution:
    def isValidSudoku(self, board) -> bool:
        # Validate Rows
        for i in range(9):
            s = set()
            for j in range(9):
                num = board[i][j]
                if num in s:
                    return False
                elif num != ".":
                    s.add(num)

        # Validate Columns
        for i in range(9):
            s = set()
            for j in range(9):
                num = board[j][i]
                if num in s:
                    return False
                elif num != ".":
                    s.add(num)

        # Validate Boxes
        starting_positions = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                starting_positions.append([i, j])
        print(starting_positions)
        for i, j in starting_positions:
            s = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    num = board[r][c]
                    if num in s:
                        return False
                    elif num != ".":
                        s.add(num)

        return True


Solution().isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

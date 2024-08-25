class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []

        combinations = []
        solution = []
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)

        def backtrack(i=0):
            if i == n:
                solution.append("".join(combinations))
                return

            for letter in phone_dict[digits[i]]:
                combinations.append(letter)
                backtrack(i + 1)
                combinations.pop()

        backtrack(0)
        return solution


print(Solution().letterCombinations("23"))

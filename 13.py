class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = len(s) - 1
        num = 0
        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1:
                num = num + roman_dict[s[i]]
            elif roman_dict[s[prev]] <= roman_dict[s[i]]:
                num = num + roman_dict[s[i]]
                prev = prev - 1
            else:
                num = num - roman_dict[s[i]]
                prev = prev - 1
        return num

# Sorted Array, Use Two Pointer Technique
class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[left] + numbers[right]
            if num == target:
                return left + 1, right + 1
            elif num < target:
                left = left + 1
            else:
                right = right - 1

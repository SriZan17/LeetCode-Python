# Sort the array, fix an element and then use two pointer approach to
# find the other two elements.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        solutions = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = n - 1
            while low < high:
                threeSum = nums[i] + nums[high] + nums[low]
                if threeSum == 0:
                    solutions.append([nums[i], nums[low], nums[high]])
                    low = low + 1
                    high = high - 1
                    while low < high and nums[low] == nums[low - 1]:
                        low = low + 1
                    while low < high and nums[high] == nums[high + 1]:
                        high = high - 1
                elif threeSum < 0:
                    low = low + 1
                else:
                    high = high - 1
        return solutions

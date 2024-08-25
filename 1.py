class Solution:
    def twoSum(self, nums, target: int):
        num_to_index = {}
        for i in range(len(nums)):
            num = nums[i]
            num2 = target - num
            if num2 in num_to_index:
                return [i, num_to_index[num2]]
            num_to_index[num] = i

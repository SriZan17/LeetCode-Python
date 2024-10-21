class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count = count + 1
            else:
                if count == 0:
                    candidate = num
                    count = 1
                else:
                    count = count - 1
        return candidate

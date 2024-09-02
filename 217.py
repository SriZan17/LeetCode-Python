class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        # hash = set()
        # for n in nums:
        #     if n in hash:
        #         return True
        #     else:
        #         hash.add(n)
        # return False

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        num_zeroes = 0

        for n in nums:
            if n != 0:
                product = product * n
            else:
                num_zeroes = num_zeroes + 1

        if num_zeroes == 0:
            for n in nums:
                if n == 0:
                    result.append(product)
                else:
                    result.append(product // n)
        elif num_zeroes == 1:
            for n in nums:
                if n == 0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            for n in nums:
                result.append(0)

        return result


class Solution:
    def productExceptSelf(self, nums):
        left_product = []
        right_product = []
        result = []
        for i in range(len(nums)):
            result.append(1)
        for j in range(1, len(nums)):
            left_product[j] = left_product[j - 1] * nums[j - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        for k in range(len(nums)):
            result.append(left_product[k] * right_product[k])
        return result

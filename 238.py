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

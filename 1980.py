# iterate through all the binary numbers from 0 to 2^limit
# convert the number to binary
# if number is less than limit, add 0 padding
# if the binary number is not in the list, return it


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        limit = len(nums)
        nos_binary = 2**limit
        for i in range(nos_binary):
            binary_string = format(i, "b")
            length = len(binary_string)
            if length < limit:
                diff = limit - length
                binary_string = "0" * diff + binary_string
            if binary_string not in nums:
                return binary_string

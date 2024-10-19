# Two pointer approach
# Kultiply the minimum of the two heights with the breadth to get the area.
# Move the pointer with the smaller height inwards.
class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            breadth = right - left
            if height[left] < height[right]:
                length = height[left]
                area = max(area, length * breadth)
                left = left + 1
            else:
                length = height[right]
                area = max(area, length * breadth)
                right = right - 1
        return area

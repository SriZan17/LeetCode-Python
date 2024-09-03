class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda interval: interval[0])

        for i in range(len(intervals)):
            num1 = intervals[i]
            if result != []:
                num2 = result[-1]
                if num2[1] >= num1[1]:
                    continue
                elif num2[1] >= num1[0]:
                    result.pop()
                    result.append([num2[0], num1[1]])
                else:
                    result.append(num1)
            else:
                result.append(num1)

        return result

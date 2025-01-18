from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = [0 for _ in range(100)];
        for i in range(len(nums)):
            t = nums[i]
            counter[t] += 1

        result = []

        for i in range(len(counter)):
            if counter[i] >= 2:
                result.append(i)

        return result

x = Solution()
y = [0, 1, 2, 2, 3, 3, 4]
result = x.getSneakyNumbers(y)
print(result)


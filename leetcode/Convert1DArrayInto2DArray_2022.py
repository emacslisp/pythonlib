from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        result = []

        for x in range(m):
            t = []
            for y in range(n):
                t.append(original[x*n + y])
            result.append(t)
        
        return result

s = Solution()

t = [1,1,1,1]
m = 1
n = 4

r = s.construct2DArray(t, m, n)
print(r)
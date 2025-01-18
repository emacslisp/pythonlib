from typing import List
from queue import PriorityQueue

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = PriorityQueue()
        for i in range(len(nums)):
            pq.put((nums[i], i))

        for i in range(k):
            x = pq.get();
            nums[x[1]] = x[0] * multiplier
            pq.put((nums[x[1]], x[0]))

        return nums

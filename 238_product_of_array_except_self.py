import array
import bisect
import collections
from collections import Counter
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])

        suffix = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i])
        suffix.reverse()

        result = [1] * len(nums)
        result[0] = suffix[1]
        result[len(nums) - 1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]

        return result

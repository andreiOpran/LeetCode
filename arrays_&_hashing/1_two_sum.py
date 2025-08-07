import array
import bisect
import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            aux = target - nums[i]
            if aux in hash:
                return [hash[aux], i]
            hash[nums[i]] = i


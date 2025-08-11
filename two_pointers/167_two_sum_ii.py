import array
import bisect
import collections
from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while True:
            auxSum = numbers[i] + numbers[j]

            if auxSum == target:
                return [i + 1, j + 1]

            if auxSum > target:
                j -= 1
            else:
                i += 1

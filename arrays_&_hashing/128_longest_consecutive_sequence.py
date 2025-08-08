import array
import bisect
import collections
from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        max_len = 0

        for num in hash:
            if (num - 1) not in hash:
                len = 1
                i = num + 1
                while True:
                    if i in hash:
                        len += 1
                        i += 1
                    else:
                        break
                max_len = max(max_len, len)

        return max_len


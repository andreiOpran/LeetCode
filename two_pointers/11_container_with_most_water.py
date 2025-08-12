import array
import bisect
import collections
from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxArea = -1
        while i < j:
            current = (j - i) * min(height[i], height[j])
            maxArea = max(current, maxArea)
            if height[i] <= height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
        return maxArea


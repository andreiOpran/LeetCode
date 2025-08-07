import array
import bisect
import collections
from collections import Counter
from typing import List

class Solution:
    """
    [abc, abcd] -> 3#abc4#abcd
    """
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    """
    3#abc4#abcd -> [abc, abcd]
    """
    def decode(self, str):
        result, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            result.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return result

import array
import bisect
import collections
from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in hash:
                hash[key] = []
            hash[key].append(str)

        # result = []
        # for key in hash.keys():
        #     result.append(hash[key])
        # return result
        return list(hash.values())

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            hash[tuple(count)].append(str)
        return list(hash.values())
'''

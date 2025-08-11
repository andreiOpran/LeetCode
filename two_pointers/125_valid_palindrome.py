import array
import bisect
import collections
from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(len(cleaned) // 2):
            j = len(cleaned) - i - 1
            if cleaned[i] != cleaned[j]:
                return False
        return True

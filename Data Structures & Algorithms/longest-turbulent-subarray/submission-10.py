from functools import cache

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        @cache
        def longest(prev, i):
            if i == n:
                return 0

            if i == n - 1:
                return 1

            if arr[i] == arr[i+1]:
                return 1

            dif = 0 if arr[i+1] == arr[i] else (-1 if arr[i+1] - arr[i] < 0 else 1)

            if prev == None:
                return 1 + longest(dif, i+1)
            
            if dif * prev >= 0:
                return 1
            
            return 1 + longest(dif, i+1)
        
        max_len = 0
        for i in range(len(arr)):
            max_len = max(max_len, longest(None, i))

        return max_len

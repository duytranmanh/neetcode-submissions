class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def longest(prev, arr):
            if len(arr) == 0:
                return 0

            if len(arr) == 1:
                return 1

            if arr[0] == arr[1]:
                return 1

            if prev == None:
                return 1 + longest(arr[1] - arr[0], arr[1:])
            
            dif = arr[1] - arr[0]

            if dif * prev >= 0:
                return 1
            
            return 1 + longest(arr[1] - arr[0], arr[1:])
        
        max_len = 0
        for i in range(len(arr)):
            max_len = max(max_len, longest(None, arr[i:]))

        return max_len
            
            
            
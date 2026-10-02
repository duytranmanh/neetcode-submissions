from functools import cache
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @cache
        def reach(i, minJump, maxJump):
            if i >= len(s) or s[i] == "1":
                return False

            if i == len(s) -1:
                return True

            for step in range(i + maxJump, i + minJump -1, -1):
                if reach(step, minJump, maxJump):
                    return True

            return False
        
        return reach(0, minJump, maxJump)
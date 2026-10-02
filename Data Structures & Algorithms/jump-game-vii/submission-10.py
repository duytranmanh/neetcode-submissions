
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        curr = 0
        reachable = [False] * len(s)
        reachable[0] = True
        numReachable = 0

        for i in range(1, len(s)):
            l = i - maxJump
            r = i - minJump

            if r >= 0 and reachable[r]:
                numReachable += 1

            if l > 0 and reachable[l - 1]:
                numReachable -= 1
            
            if s[i] == "0" and numReachable > 0:
                reachable[i] = True
        
        print(reachable)

        return reachable[-1]

            



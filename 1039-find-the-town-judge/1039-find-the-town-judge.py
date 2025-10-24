from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # trusted
        trusted = defaultdict(int)
        #truster
        truster = defaultdict(int) 
        
        for a, b in trust:
            # a trusts b 
            truster[a] += 1
            
            # b trusts a
            trusted[b] += 1
            
        for i in range(0, n):
            trusts_nobody = truster[i+1] == 0
            
            is_trusted = trusted[i+1] == n - 1
            
            if trusts_nobody and is_trusted:
                return i+1
                
        return -1
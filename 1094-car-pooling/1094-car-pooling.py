'''
best way is to have an array each index is each km
for each one + ppl get on adn then - is ppl off

loop and if the cap is ever over then False

'''

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        eachkm = [0] *1001

        for trip in trips:
            eachkm[trip[1]] += trip[0]
            eachkm[trip[2]] -= trip[0]

        currcap = 0

        for km in eachkm:
            currcap += km
            if currcap > capacity:
                return False
        return True
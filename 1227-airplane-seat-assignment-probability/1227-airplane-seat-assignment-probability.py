'''
say there is 5 ppl
1st = 100
2nd = 50
3rd = 50

a person either gets their seat or they dont

its a pick a card but dont replace
'''

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return float(1)
        else:
            return float(0.5)
        
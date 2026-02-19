'''
just one for loop
for each i you go until that i isnt null
have a counter for 0's and 1's and result

if i = 0 then see how many zeros in a row there are
, then imediately after the zeros there has to be the same amnt of 1's

maybe a stack for each
so add all the 0's or 1's then when it swaps pop and if it ends up being empty before then its += 1

this would be a on^2 approach tho

 if there are 3 0 and 2 1 tjem tje poss are 2
 same with any combo its the min, so have 2 traclers



'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        count_curr = 1
        count_next = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count_curr += 1
            else:
                res += min(count_curr, count_next)
                count_next = count_curr
                count_curr = 1
        res += min(count_curr, count_next)

        return res
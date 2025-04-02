class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        score = 0
        max_score = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = zeros + ones
            if score > max_score:
                max_score = score
        return max_score

        
            
        





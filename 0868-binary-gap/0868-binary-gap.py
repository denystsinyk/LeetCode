class Solution:
    def binaryGap(self, n: int) -> int:
        num = bin(n)[2:]
        print(num)

        longest_gap = 0
        prev_one = -1
        for i in range(len(num)):
            if num[i] == '1':
                if prev_one != -1:
                    # current i - last seen
                    longest_gap = max(longest_gap, i-prev_one)
                prev_one = i
            

        return longest_gap
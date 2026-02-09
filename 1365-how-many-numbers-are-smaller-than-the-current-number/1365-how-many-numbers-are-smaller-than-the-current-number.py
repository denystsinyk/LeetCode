class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        result = []

        for value in nums:
            freq[value] += 1

        smaller_count = [0] * 101
        running = 0

        for v in range(len(smaller_count)):
            smaller_count[v] = running
            running += freq[v]

        for value in nums:
            result.append(smaller_count[value])

        return result
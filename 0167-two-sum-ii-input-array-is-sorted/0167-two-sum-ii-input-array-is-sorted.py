class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer and get the sum, if bigger than target then move right inwards
        # less than would move the left inwards

        l, r = 0, len(numbers) -1
        curr = 0

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr < target:
                l += 1
            elif curr > target:
                r -= 1
            else:
                return [l+1, r+1]
            

            
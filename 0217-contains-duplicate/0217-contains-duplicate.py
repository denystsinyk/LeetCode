class Solution:
    from collections import defaultdict

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            if num not in seen:
                seen[num] += 1
            else:
                return True
        return False

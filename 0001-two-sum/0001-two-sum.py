class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in d:
                return [i,d[dif]]
            else:
                d[nums[i]] = i

        
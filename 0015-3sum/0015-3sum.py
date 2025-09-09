class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        seenOuter = set()
        for i in range(len(nums)):
            if nums[i] not in seenOuter:
                target = -nums[i]
                seen = set()
                for j in range(i+1, len(nums)):
                    current = [nums[i], target - nums[j], nums[j]]
                    if target - nums[j] in seen:
                           
                        if len(result) == 0:
                            result.append(current)
                        if len(result) > 0 and result[-1] != current:
                            result.append(current)


                    seen.add(nums[j])
            seenOuter.add(nums[i])
        return result

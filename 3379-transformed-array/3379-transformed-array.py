class Solution:

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        result = [0] * n
        # mover func

        for i in range(len(nums)):
            if nums[i] == 0:
                # set result[i] to nums[i]
                result[i] = nums[i]
            else:
                res_index = (nums[i] + i) % n
                result[i] = nums[res_index]



        return result
        
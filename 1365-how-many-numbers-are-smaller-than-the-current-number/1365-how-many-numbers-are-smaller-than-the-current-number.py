class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # loop through each num
        # for each num run another loop and if smaller add one
        # we could also sort it, then anything after is larger
        # since we cant use a dict we could also do a counter

        res = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]: 
                    count += 1
            res.append(count)
        return res


        
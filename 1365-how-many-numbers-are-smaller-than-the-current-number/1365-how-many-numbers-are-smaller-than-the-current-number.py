class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # loop through each num
        # for each num run another loop and if smaller add one
        # we could also sort it, then anything after is larger
        # since we cant use a dict we could also do a counter

        res = [0] * len(nums) # this did not speed it up

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]: 
                    count += 1
            res[i] = count
        return res

        # to make it faster we could sort it
        
        



        
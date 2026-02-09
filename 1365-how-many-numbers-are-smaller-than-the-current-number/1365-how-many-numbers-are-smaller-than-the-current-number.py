class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # loop through each num
        # for each num run another loop and if smaller add one
        # we could also sort it, then anything after is larger
        # since we cant use a dict we could also do a counter

        # res = [0] * len(nums) # this did not speed it up

        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if i != j and nums[j] < nums[i]: 
        #             count += 1
        #     res[i] = count
        # return res

        # to make it faster we could sort it then get the first
        # occurance and that index is how many nums are smaller than it
        counts = {}
        sorted_nums = sorted(nums)

        for i in range(len(nums)):
            if sorted_nums[i] not in counts:
                counts[sorted_nums[i]] = i
        # basically if the num is not in the dictionary, 
        # then we set its value to the index, bc thats how many are smaller than it
        res = []
        for num in nums:
            count = counts[num] # we get the count that are smaller
            res.append(count)
            # we dont have to worry abt it being out of order bc we just loops through nums
            # and then like count is the nums so it works out
        return res
        



        
        



        
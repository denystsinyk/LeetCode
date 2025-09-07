class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # using a dictionary to record all the values we have seen as looping
        # also keeps track of those index

        for index, value in enumerate(nums): # loop through keeps track of value and index
            diff = target - value # difference is useful to determine what number we need
            if diff in seen: # if we have seen it then we can return
                return [seen[diff],index]
            seen[value] = index # if we havent seen it yet then add to the seen

            # we want to add the value map to index since we also want the diff to match
            # wont be possible to map the other way around

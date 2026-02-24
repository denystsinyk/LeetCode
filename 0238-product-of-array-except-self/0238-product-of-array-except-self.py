'''

INPUT : Array of ints
OUTPUT : An Array where the value at index is the product of all other i's

examples
    [1,2,3,4]
    [24,12,8,6]

approaches
    brute force - too slow
        for each element loop through kinda thing

    get total sum and divide - cant use division operation

    pre compute something
        loop once and get the product before (gives us half)
        loop again and get sums after (other half)
        then add them togetehr



'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums))

        pre_prod = 1
        post_prod = 1
        # loop and get the product before
        for i in range(len(nums)):
            answer[i] *= pre_prod
            pre_prod *= nums[i]

                
        # post prod and multiple to what we have rn
        # iterate backwards
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= post_prod
            post_prod *= nums[i]

        '''
            so we go backwards and then the right
            is the prod of all that we have seen
        '''
         
        return answer























        
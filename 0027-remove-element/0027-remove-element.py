class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        k = len(nums)
        while l <= r:
            if nums[r] == val:
                r -= 1
                k -= 1
                print(nums)
                continue
            if nums[l] == val:
                k -= 1
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
            else:
                l += 1
            print(nums)
        print(k)
        return k 
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        int = str(x)
        left = 0
        right = len(int) - 1

        while left < right:
            if int[left] != int[right]:
                return False
            left += 1
            right -= 1

        return True




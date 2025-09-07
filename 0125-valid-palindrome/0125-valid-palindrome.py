class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char for char in s if char.isalnum()).lower()
        # .isalnum() checks if anything is alpha numeric
        # char for char in s = takes each character in s 
        # if in char.isalum then joins to the string
        # .lower to account for capitals

        left, right = 0, len(cleaned_string) - 1 # since len() gives num of chars need
        # to convet tho index form ... ie. -1
        while left < right: # no need to use a for loop since the 2 points converge
        # we want to keep doing this until they touch, but not == bc they can skip
            if cleaned_string[left] == cleaned_string[right]: 
                # check opposite ends to make sure they match
                left += 1 
                right -= 1
                # shift each inside
            else:
                return False
        return True
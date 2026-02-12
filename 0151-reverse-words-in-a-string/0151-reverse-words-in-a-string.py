class Solution:
    def reverseWords(self, s: str) -> str:
        # trim and split by spaces
        # then 2 pointers to swap
        s = s.strip()
        words = s.split()

        print(words)

        l, r = 0 , len(words) - 1
        while l < r:
            temp = words[l]
            words[l] = words[r]
            words[r] = temp
            l += 1
            r -= 1
        
        return ' '.join(word for word in words)
        
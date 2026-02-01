class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # ord('a')
        result = float('inf')
        answer = None
        for letter in letters:
            if letter == target:
                continue
            count = ord(letter) - ord(target)
            if count < 0:
                continue
            
            print(count)
            print(result)
            if count < result:
                result = count
                answer = letter
        
        if answer == None:
            return letters[0]
        return answer
        
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                toPrint = ""
                while stack[-1] != "[":
                    toPrint = stack.pop() + toPrint
                stack.pop()
                numTimes = ""
                while stack and stack[-1].isdigit():
                    numTimes = stack.pop() + numTimes
                toPrint = int(numTimes) * toPrint
                stack.append(toPrint)
            
        return "".join(stack)
                


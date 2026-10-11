'''
input: string with the rule of k[encode]
output: decode the string so simplify all the brackets

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

approaches:
    stack - 
        push onto stack so that we can pop off the nums to translae them

'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                decode = ""
                while stack and stack[-1] != "[":
                    decode = stack.pop() + decode
                stack.pop() # left bracket
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                decode = int(num) * decode
                stack.append(decode)
        return "".join(stack)

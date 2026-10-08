'''

add all to stack ifn not )or, if ) then pop until ( and if , then contniue


'''
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char == ",":
                continue
            if char != ")":
                stack.append(char)
            else:
                toCheck = []
                while stack[-1] != "(":
                    toCheck.append(stack.pop())
                stack.pop()
                op = stack.pop()
                
                if op == "|":
                    res = "t" if "t" in toCheck else "f"
                elif op == "&":
                    res = "t" if "f" not in toCheck else "f"
                else:
                    res = "t" if toCheck[0] == "f" else "f"
                stack.append(res)
        return stack[-1] == "t"
                    

        
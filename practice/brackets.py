from collections import deque
from typing import List
def valid_brackets(list):

    brackets = {
        ")": "(", "}": "{", "]": "["
    }
    opens = {"(", "{", "["}
    closes = {")", "]", "}"}
    out: List[bool] = []

    for s in list:
        stack = deque()
        ok = True 
        for char in s:
            if char in opens:
                if char == "[" and stack and stack[-1] == "(":
                    ok = False
                    break
                stack.append(char)
            elif char in closes:
                if not stack:
                    ok = False 
                    break
                if stack.pop() != brackets[char]:
                    ok = False
                    break 
            else:
                ok = False
                break 
        if ok and stack:
            ok = False 
            
        out.append(ok)
    return out
                

Input = ["()", "{[()]}", "([{}])", "({[]})", "[({})]", "([)]", ""]
print(valid_brackets(Input))
    

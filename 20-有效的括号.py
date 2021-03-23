"""
解题思路；
1. 使用栈的特性
"""

def isValid(self, s: str) -> bool:
    dictMap = {
        '{': '}',  
        '[': ']', 
        '(': ')', 
        }
    stack = ['*']
    for c in s:
        if c in dictMap: 
            stack.append(dictMap[c])
            continue
        if stack.pop() != c:
            return False
    return len(stack) == 1

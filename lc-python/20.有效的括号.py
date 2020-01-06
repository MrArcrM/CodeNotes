#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Stack
        #       !: check if stack is empty before stack.pop()      
        stack = []
        d = { '(' : ')', '[' : ']', '{' : '}' }
        for c in s:
            if c in d.keys():
                stack.append(d[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
        
        return len(stack) == 0

        # 2. Brute Force
        #       Replace valid char pairs to empty str
        # while '[]' in s or '()' in s or '{}' in s:
        #     s = s.replace('[]', '').replace('()', '').replace('{}', '')
        
        # return not len(s)


# @lc code=end


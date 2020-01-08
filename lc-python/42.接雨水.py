#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: 'List[int]') -> int:
        ans = 0
        stack = []
        for i, n in enumerate(height):
            while stack and n > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    h = min(n, height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1
                    ans += h * w
            
            stack.append(i)
        
        return ans


# @lc code=end


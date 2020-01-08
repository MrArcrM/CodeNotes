#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        d = deque()
        output = []

        for i, n in enumerate(nums):
            while d and n > nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                output.append(nums[d[0]])
            
        return output

# @lc code=end
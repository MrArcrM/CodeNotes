#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        dic = {}
        for i, n in enumerate(nums):
            if n in dic.keys():
                return [dic[n], i]
            else:
                dic[target - n] = i
        
        return [-1, -1]


# @lc code=end


#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        p = 1 if len(nums) > 0 else 0
        for num in nums:
            if num > nums[p-1]:
                nums[p] = num
                p += 1
            
        return p


# @lc code=end


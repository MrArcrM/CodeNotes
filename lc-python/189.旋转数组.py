#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k : ] + nums[ : n-k] 


        
# @lc code=end


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 3)
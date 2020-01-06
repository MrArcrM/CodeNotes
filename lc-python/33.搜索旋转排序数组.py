#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target and target < nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1        


if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 3]
    target = 5
    s.search(nums, target)


# @lc code=end


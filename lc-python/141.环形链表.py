#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False

        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: 
                return True
        
        return False



# @lc code=end


#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: # Has cycle
                walker = head
                while walker != runner:
                    walker = walker.next
                    runner = runner.next
                
                return walker
        
        return None




# @lc code=end


#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        for i in range(k):
            if not p: return head
            p = p.next
        pre = self.reverseKGroup(p, k)
        cur = head
        nxt = None
        while cur != p:
            nxt = cur.next
            cur.next = pre
            pre = cur 
            cur = nxt
        return pre


# @lc code=end


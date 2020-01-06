#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start

class DbListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # insert in top
            top_node = self.top.next
            self.top.next = cur
            cur.next = top_node
            top_node.prev = cur
            cur.prev = self.top
            return self.hkeys[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]        
            cur.val = value
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # insert in top 
            top_node = self.top.next
            self.top.next = cur
            cur.next = top_node
            top_node.prev = cur
            cur.prev = self.top
        else:
            cur = DbListNode(key, value)
            self.hkeys[key] = cur
            top_node = self.top.next
            self.top.next = cur
            cur.next = top_node
            top_node.prev = cur
            cur.prev = self.top
            # capacity problem
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


## 06-LinkedList-1

> 如何用数组实现LRU缓存策略？

```python

class LRUCache:
    def __init__(self, maxLen):
        self.arr = [0] * maxLen
        self.maxLen = maxLen
        self.curSize = 0

    def insert(self, val):
        idx = self.search(val)
        if idx > 0:
            for i in range(p-1, -1, -1):
                arr[i+1] = arr[i]
            arr[0] = val
        elif curSize < maxLen:
            arr[curSize] = val
            curSize += 1
        else:
            arr[curSize-1] = val

    def  delete(self, val):
        idx = self.search(val)
        if idx >= 0:
            for i in range(p+1, curSize):
                arr[i-1] = arr[i]
            curSize -= 1
    
    def search(self, val):
        for i in range(curSize):
            if arr[i] == val:
                return i
        return -1
```



> 单链表如何判断回文串？

```python
# O(n) Time, O(n) Space
def isPalindrome(head):
    s1 = ""
    s2 = ""
    while head is not None:
        s1 = head.val + s1
        s2 = s2 + head.val
        head = head.next
    return s1 is s2
```


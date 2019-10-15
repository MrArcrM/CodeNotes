## 07-LinkedList-2

> 单链表反转

```python
def reverse(head):
    if head is None or head.next is None: return head
    
    pre = None
    cur = head
    nxt = cur.next
    while cur.next is not None:
        pre = cur
        cur = nxt
        nxt = nxt.next
    return cur
```

> 链表中环的检测

```python
def hasCircle(head):
    if head is None or head.next is None: return False
    
    slow = head
    fast = head.next
    
    while slow is not None:
        if slow == fast: return True
        slow = slow.next
        fast = fast.next
        if fast is None: return True
        fast = fast.next
    
    return False
```

> 两个有序的链表合并

```python
def merge(h1, h2):
	pHead = Node(-1)
    p = pHead
    while h1 is not None and h2 is not None:
        if h1.val < h2.val:
            p.next = h1
        else: p.next = h2
        
        h1 = h1.next
        h2 = h2.next
        p = p.next
    
    if h1 is not None:
        p.next = h1
    
    if h2 is not None:
        p.next = h2
    
    return pHead.next    
    
```

> 删除链表倒数第n个节点

```python
def del_from_end(head, n):
    if head is None or n <= 0: return None
    
	tot = 0
    p = head
    while p is not None:  # 计算链表长度
        p = p.next
        tot += 1
        
    if tot < n: return None
    elif tot == n:  # 删除第一个节点
        head = head.next
        return head
    
    preCount = tot - n  # 待删除的节点的前一个结点，正数是第preCount个
    p = head
    preCount -= 1  # 因为从head开始计，所以preCount要减1
    while preCount > 0:
        preCount -= 1
        p = p.next
    p.next = p.next.next  # 这里p是待删除的节点的前一个结点  
    
    return head
```

> 求链表的中间节点

```python
def mid(head):
    if head is None or head.next is None: return head
    
    slow = head
    fast = head.next
    
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
        if fast is None: break
        fast = fast.next
    
    return slow
```


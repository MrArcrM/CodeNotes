#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        # if k <= 0: throw exception
        self._size = 0
        self._front, self._rear = 0, 0
        self._data = [-1] * k
        self._capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False  
        if not self.isEmpty():
            self._front = (self._front - 1) % self._capacity

        self._data[self._front] = value
        self._size += 1

        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if not self.isEmpty():
            self._rear = (self._rear + 1) % self._capacity
        
        self._data[self._rear] = value
        self._size += 1

        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self._data[self._front] = -1
        if self._size > 1:
            self._front = (self._front + 1) % self._capacity
        self._size -= 1

        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self._data[self._rear] = -1
        if self._size > 1:
            self._rear = (self._rear - 1) % self._capacity
        self._size -= 1

        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self._data[self._front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self._data[self._rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == self._capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end


if __name__ == '__main__':
    obj = MyCircularDeque(2)
    param_1 = obj.insertFront(7)
    param_2 = obj.deleteLast()
    param_3 = obj.getFront()
    param_4 = obj.insertLast(5)
    param_5 = obj.insertFront(0)
    param_6 = obj.getFront()
    param_7 = obj.getRear()
    param_8 = obj.getFront()    
    param_9 = obj.getFront()
    param_10 = obj.getRear()
    param_11 = obj.insertLast(0)
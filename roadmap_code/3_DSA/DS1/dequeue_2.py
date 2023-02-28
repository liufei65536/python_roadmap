class Deque:
    def __init__(self, size):
        self.size = size
        self.items = [-1] * size
        self.front = -1
        self.rear = 0

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)

    def isEmpty(self):
        return self.front == -1

    def addFront(self, item):
        if self.isFull():
            return None
        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.items[self.front] = item

    def addRear(self, item):
        if self.isFull():
            return None
        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.items[self.rear] = item

    def removeFront(self):
        if self.isEmpty():
            return None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1

    def removeRear(self):
        if self.isEmpty():
            return None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.items[self.front]

    def getRear(self):
        if self.isEmpty() or self.rear < 0:
            return -1
        return self.items[self.rear]

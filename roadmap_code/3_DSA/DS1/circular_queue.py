# Circular Queue implementation in Python


class MyCircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    # Insert an element into the circular queue
    def enqueue(self, data):
        if self.is_full():
            print("The circular queue is full\n")
            return None
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if self.is_empty():
            print("The circular queue is empty\n")
            return None

        temp = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return temp

    def __str__(self):
        if self.head == -1:
            return "No element in the circular queue"
        elif self.tail >= self.head:
            return str(self.queue[self.head: self.tail + 1])
        else:
            return str(self.queue[self.head: self.size] + self.queue[:self.tail + 1])


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
for i in range(1,6):
    obj.enqueue(i)
print("Initial queue")
print(obj)

obj.dequeue()
print("After removing an element from the queue")
print(obj)

obj.enqueue(6)
print("After insert an element to the queue")
print(obj)
obj.enqueue(7)
print("After insert an element to the queue")
print(obj)
for _ in range(3):
    obj.dequeue()
print(obj)


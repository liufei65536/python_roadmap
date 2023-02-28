# Queue implementation in Python

class Queue:

    def __init__(self,size):
        self.queue = [None]*size
        self.size = size
        self.front = -1 # 头
        self.rear = -1 # 尾

    def is_full(self):
        return  self.front == 0 and self.rear == self.size -1

    def is_empty(self):
        return  self.front == -1

    # Add an element
    def enqueue(self, item):
        if self.is_full():
            print("queue is full, cancel enqueue")
            return None
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item

    # Remove an element
    def dequeue(self):
        if self.is_empty():
            print("queue is empty, cancel dequeue")
            return None
        res = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return res


    # Display  the queue
    def __str__(self):
        return str(self.queue[self.front:self.rear+1])



q = Queue(10)
for i in range(1,12):
    q.enqueue(i)


print(q)
q.dequeue()
print("After removing an element")
print(q)



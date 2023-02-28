# Stack
class Stack2:
    def __init__(self, size):
        self.size = size
        self.stack = [None]* size
        self.top = -1

    def push(self, ele):
        if self.is_full():
            print("stack is full, cancel push")
            return
        self.top += 1
        self.stack[self.top] = ele

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        res = self.stack[self.top]
        self.top -= 1
        return res

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size -1

    def __str__(self):
        return str(self.stack[:self.top+1]) if self.top != -1 else str([])


if __name__ == '__main__':
    stack = Stack2(10)
    for i in range(11):
        stack.push(str(i))
    print("stack  " + str(stack))
    print("popped item: " + stack.pop())
    print("stack after popping an element: " + str(stack))

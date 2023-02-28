# Stack
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    stack = Stack(10)
    for i in range(15):
        stack.push(str(i))
    print("stack  " + str(stack))
    print("popped item: " + stack.pop())
    print("stack after popping an element: " + str(stack))

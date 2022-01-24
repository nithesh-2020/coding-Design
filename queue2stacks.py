class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while (bool(self.stack1)):
            self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        while (bool(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return temp

    def peek(self) -> int:
        while (bool(self.stack1)):
            self.stack2.append(self.stack1.pop())
        temp = self.stack2[-1]
        while (bool(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return temp

    def empty(self) -> bool:
        return not bool(self.stack1)

if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(3)
    q.push(4)
    print(q.empty())
    print(q.pop())
    print(q.peek())

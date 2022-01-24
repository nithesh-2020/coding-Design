class minstack:
    min = float('inf')
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int):
        if (self.min >= val):
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self):
        temp = self.stack[-1]
        self.stack.pop()
        if (temp==self.min):
            self.min = self.stack[-1]
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min

if __name__ == '__main__':
    minstack1 = minstack()
    minstack1.push(3)
    minstack1.push(-1)
    print(minstack1.getMin())


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return self.stack[-2]



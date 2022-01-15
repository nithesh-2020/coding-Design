# MinStack leetcode problem

#Approach 1: using extra stack

#Time : every function executes in constant time
#space: O(N) for using extra stack

'''class MinStack:

    def __init__(self):
        self.st=[]
        self.min_st=[]
    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.min_st.append(val)
        else:
            self.st.append(val)
            
            if val<=self.min_st[-1]:
                self.min_st.append(val)
    def pop(self) -> None:
        if self.st[-1]==self.min_st[-1]:
            self.st.pop()
            self.min_st.pop()
        else:
            self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        
        return self.min_st[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()'''

# Approach 2: without using extra stack
#Time : every function executes in constant time
#space: O(N) for using extra stack

class MinStack:

    def __init__(self):
        
        self.min=math.inf
        self.min_stack=[self.min]
        
    def push(self, val: int) -> None:
        if self.min>=val:
            self.min_stack.append(self.min)
            self.min=val
        self.min_stack.append(val)
        # print(self.min_stack)
        
    def pop(self) -> None:
        
        temp=self.min_stack[-1]
        self.min_stack.pop()
        if temp==self.min:
            self.min=self.min_stack[-1]
            self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

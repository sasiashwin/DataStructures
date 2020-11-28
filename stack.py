from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        return self.container.append(val)
    def pop(self,val):
        return self.container.remove(val)
    def peek(self):
        return self.container[-1]
    def length(self):
        return len(self.container)
    def isempty(self):
        return len(self.container)==0
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop(20)
print(s.isempty())
print(s.length())
print(s.container)

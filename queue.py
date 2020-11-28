from collections import deque
class queue:
    def __init__(self):
        self.container=deque()
    def insert(self,val):
        return self.container.appendleft(val)
    def pop(self):
        return self.container.pop()
    def isempty(self):
        return len(self.container)==0
    def peek(self):
        return self.container[-1]
s=queue()
s.insert("sasi")
s.insert("ram")
s.insert("99")
s.pop()
print(s.isempty())
print(s.peek())
print(s.container)

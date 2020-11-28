from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        return self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def length(self):
        return len(self.container)
    def isempty(self):
        return len(self.container)==0
s=Stack()
string = "We will conquere COVID-19"
for i in string:
    s.push(i)
print(s.container)
while(s.isempty()==False):
    print(s.pop(),end="")

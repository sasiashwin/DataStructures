class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def insert_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr=self.head
        ll = ''
        while itr:
            ll += str(itr.data)+'-->'
            itr = itr.next
        print(ll)
l = LinkedList()
l.insert_begin(10)
l.insert_begin(20)
l.insert_begin(30)
l.insert_end(40)
l.print()

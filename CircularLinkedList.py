class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next
              
class CircularLinkedList:
    def __init__(self,head=None):
        self.head = head

    def insetAtEnd(self,value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            temp.next = self.head
            return
            
        t1 = self.head
        while(t1.next != self.head):
            t1 = t1.next
            
        t1.next = temp
        temp.next = self.head


    def printCLL(self):
        t = self.head
        while(t.next != self.head):
            print(t.data)
            t = t.next
        print(t.data)

obj = CircularLinkedList()
obj.insetAtEnd(10)
obj.insetAtEnd(30)
obj.printCLL()
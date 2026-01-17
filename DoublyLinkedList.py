class Node:
    def __init__(self,value=None):
        self.prev = None
        self.data = value
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return 
        
        t = self.head 
        while(t.next != None):
            t = t.next
        
        t.next = temp
        temp.prev = t
    
    def insertAtBeginning(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp 
            self.head = temp
            return
    
    def insertAtMiddle(self,value,loc):
        temp = Node(value)
        t = self.head
        while(t.next != None):
            if(t.data == loc):
                break
            else:
                t = t.next
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deletionLinkedList(self,value):
        t = self.head
        if (self.head == None):
            print("Linked List is empty")
            return
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if(t.data == value):
            t.prev.next = None
            return
                
    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data)
            t = t.next
        print(t.data)
    
obj = DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(50)
obj.insertAtBeginning(4)
obj.insertAtMiddle(110,20)
obj.deletionLinkedList(30)
obj.printDLL()




class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_end(self,data):
        temp=self.start
        newnode=Node(data)            
        if not self.is_empty():
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
        else:
            self.start=newnode    
    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')        
            temp=temp.next
    def delete_end(self):
        if self.start is None:
            pass        
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                prev=temp
                temp=temp.next
            prev.next=None
            print("node %d is delete: ",temp.item)        
list=SLL()            
list.insert_end(10)
list.insert_end(20)
list.insert_end(30)
list.print()
print()
list.delete_end()
list.print()
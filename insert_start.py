class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        newnode=Node(data,self.start)            
        self.start=newnode
    def delete_from_start(self):
        temp=self.start
        if self.start is not None:
            pass
        self.start=self.start.next
        print("node %d is delete: ",temp.item)    
    def print(self):
        temp=self.start    
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
list=SLL()            
list.insert_at_start(10)
list.insert_at_start(20)
list.insert_at_start(30)
list.print()
print()
list.delete_from_start()
list.print()
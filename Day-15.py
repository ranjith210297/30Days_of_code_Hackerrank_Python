class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        
        #now check if the linked list is empty or not
        if head is None:
            head = new_node
        else:
            current_node = head
            #checking for the last node's address using current_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 
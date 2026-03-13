class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None
    

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def find_length(self, node): 

        if node is None: 
            return 0
        
        count = 1
        
        # Traverse left
        
        current = node.prev
        while current is not None:
            count += 1 
            current = current.prev

        # Traverse right
        current = node.next
        while current is not None:
            count += 1 
            current = current.next

        return count 



# Driver code 
list1 = DoublyLinkedList()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Link nodes: 1 <-> 2 <-> 3
n1.next = n2

n2.prev = n1
n2.next = n3

n3.prev = n2

n3.next = n4
n4.prev = n3

n4.next = n5
n5.prev = n4

list1.head = n1

# Call function using middle node
print(list1.find_length(n3))  # Output: 5
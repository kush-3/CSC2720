class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 


class LinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0 
    
    def is_empty(self):
        return self.head is None  

    def concatenate(self, list1, list2, len1, len2):

        # Handle empty lists
        if list1.head is None:
            return list2.head
        if list2.head is None:
            return list1.head

        # If list1 is shorter → list1 + list2
        if len1 < len2:
            current = list1.head
            while current.next is not None:
                current = current.next
            current.next = list2.head
            return list1.head

        # Otherwise → list2 + list1
        
        else:
            current = list2.head
            while current.next is not None:
                current = current.next
            current.next = list1.head
            return list2.head


# Driver code 


list1 = LinkedList()
list1.head = Node(1)
list1.head.next = Node(2)
list1.head.next.next = Node(3)

list2 = LinkedList()
list2.head = Node(4)
list2.head.next = Node(5)

ll = LinkedList()
new_head = ll.concatenate(list1, list2, 3, 2)

# Print result
current = new_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
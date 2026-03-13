class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        current = self.head
        print("Linked List: [ ", end="")
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print("]")
        print(f'head = {self.head.value} tail = {self.tail.value} size = {self.size}')

    def addFirst(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def add(self, k, value): # add the node at index k
        if k < 0 or k > self.size:
            raise IndexError('Index out of bounds!')

        if k == 0:
            self.addFirst(value)
            return
        node = Node(value)
        current = self.head
        i = 0

        #Traverse to the (k-1)th node
        while i < k-1:
            current = current.next
            i += 1

        # insert the new node after (k-1)th node
        node.next = current.next
        current.next = node

        #update tail if the inserted node is the last one
        if current == self.tail:
            self.tail = node
        self.size += 1

    def reverse(self):
        # Reverse the linked list in-place
        current = self.head
        self.tail = self.head  # original head becomes tail after reversal
        previous = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # previous will be the new head
        self.head = previous

# Driver code
ll = LinkedList()
# add 10 nodes to the linked list
for i in range(10):
    print(f'>>> Inserting {i*i} as node #{i}')
    ll.add(i, i*i)
    ll.print_list()

# insert a new node with value '100' as the head
print(f'>>> Inserting {100} as node #{1}')
ll.add(0, 100)
ll.print_list()

# trying to insert at any invalid position
#ll.add(20, 200)
#ll.add(-1, 300)
print("reversing the linked list...")
print("Expected output after reversing: [ 81 64 49 36 25 9 4 1 0 100 ]")
ll.reverse()
ll.print_list()
#Exepected output:
#Linked List: [ 81 64 49 36 25 9 4 1 0 100 ]
#head = 81 tail = 100 size = 11
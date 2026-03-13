# kush patel 
# homework 1 task 3:

# initialize the node class for the circular linked list
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

def insert_val(head, value): 
    # if there is no head then create a new node and make it point to itself 
    if not head:
        new_node = Node(value)
        new_node.next = new_node 
        return new_node
    
    # traverse the cicular linked list to find the correct position to insert the new node 
    curr = head 
    while True:
        next_node = curr.next

        if curr.value <= value <= next_node.value:
            break 
        if curr.value > next_node.value:
            if value >= curr.value or value <= next_node.value:
                break
        curr = curr.next

        if curr == head:
            break
    new_node = Node(value)
    new_node.next = curr.next
    curr.next = new_node 
    return head 


# print the circulat linked list 
def print_circular(head):
    result = []
    curr = head

    while True:
        result.append(curr.value)
        curr = curr.next
        if curr == head:
            break

    print(result)


# Test case or driver code:
head = Node(3)
node2 = Node(4)
node3 = Node(1)

head.next = node2
node2.next = node3
node3.next = head

head = insert_val(head, 10)

print_circular(head)
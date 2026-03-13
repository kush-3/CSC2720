# defining of linked list stack
# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list stack class
class Linked_list_stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def top(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def display(self): 
        current = self.head
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        return stack


# driver code 
if __name__ == "__main__":
    print("=== Linked List Stack Driver Code ===")
    stack = Linked_list_stack()
    print("\nPushing to stack:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("stack after pushing:", stack.display())
    print("Pop from stack:", stack.pop())
    print("stack after pop:", stack.display())
    print("Top of stack:", stack.top())
    print("Stack size:", stack.size)
    print("Stack after all the operations:", stack.display())
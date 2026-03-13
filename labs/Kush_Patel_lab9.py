class Node:
    def __init__(self, value):
        self.value = value
        self.left = None; self.right = None


def height(node):
    if node is None:
        return -1
    elif node.left is None and node.right is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))

def find_min(node):
    if node is None:
        return None
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def find_max(node):
    if node is None:
        return None
    current = node
    while current.right is not None:
        current = current.right
    return current.value



# driver code 
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print("height of the tree is :",height(root)) # should be 2
print("minimum value in the tree is :",find_min(root)) # should be 2
print("maximum value in the tree is :",find_max(root)) # should be 20


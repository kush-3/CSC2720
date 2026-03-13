class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.right = right 
        self.left = left 
    


def evaluate(node):


# helper function to evaluate the expressino tree
    def ebaluate_helper(node):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return int(node.value)

        # recursively evalutae the left and right subtrees
        left_value = ebaluate_helper(node.left)
        right_value = ebaluate_helper(node.right)
        
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
        else:
            raise ValueError(f"Invalid operator: {node.value}")
    
    return ebaluate_helper(node)



root = Node('*')
root.left = Node('+')
root.right = Node("-")
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(2)
print(evaluate(root))
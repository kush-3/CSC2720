# Kush Patel
# Lab 14
# Check if a binary tree is a valid AVL tree


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def _is_valid_avl_helper(node, minimum, maximum):
    if node is None:
        return True, 0
    if not (minimum < node.value < maximum):
        return False, 0
        
    left_is_valid, left_height = _is_valid_avl_helper(node.left, minimum, node.value)
    right_is_valid, right_height = _is_valid_avl_helper(node.right, node.value, maximum)
    
    is_balanced = abs(left_height - right_height) <= 1
    is_valid = left_is_valid and right_is_valid and is_balanced
    height = 1 + max(left_height, right_height)

    return is_valid, height


def is_valid_AVL_tree(root):
    """
    Returns True if the tree is a valid AVL tree, False otehrwise.
    """
    
    is_valid, height = _is_valid_avl_helper(root, float("-inf"), float("inf"))
    return is_valid




# Test Case 1: A Valid AVL Tree
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(5)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(8)


# Test Case 2: Invalid AVL Tree
# Balanced, but not a BST because 2 is in the right subtree of 3
root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(5)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)


# Test Case 3: Invalid AVL Tree
# A BST, but not balanced
root3 = TreeNode(3)
root3.left = TreeNode(1)
root3.right = TreeNode(5)
root3.right.left = TreeNode(4)
root3.right.right = TreeNode(8)
root3.right.right.right = TreeNode(9)


print("Test Case 1 - Valid AVL Tree:", is_valid_AVL_tree(root1))
print("Test Case 2 - Balanced, but not a BST:", is_valid_AVL_tree(root2))
print("Test Case 3 - BST, but not balanced:", is_valid_AVL_tree(root3))
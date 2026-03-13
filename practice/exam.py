# q1 = 7

# q2
def reverse(arr):
    stack = stack()
    for i in arr:
        stack.append(i)
    result = []
    for i in stack:
        result.append(stack.pop())
    return result

# q3
def remove_all(stack):
    if stack is None:
        return None
    stack.pop()
    return remove_all(stack)

# q4
def insert_at(self, k, data):
    new_node = Node(data)
    if k == 1:
        new_node.next = self.head
        return new_node
    current = self.head
    for i in range(1, k-2):
        if current is None or current.next is None:
            return head, "position out of bounds"
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

# q5
def merge_sorted(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    result = []
    while list1 is not None:
        result.append(list1.val)
        list1 = list1.next
    while list2 is not None:
        result.append(list2.val)
        list2 = list2.next
    
    result.sort()
    dummy = Node(0)
    current = dummy
    for val in result:
        current.next = Node(val)
        current = current.next
    return dummy.next


# q6

def has_cycle(head):
    slow = head 
    fast = head 
    if head is None:
        return False 
    
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False


# q7
def in_order(root):
    result = []
    def dfs(node):
    # change the order of the traversal to post order or preorder whatever is asked 
        if node is None:
            return 
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


# q8
# [35, 22, _, 3, 18, 12, _]
    


class TwoStack:
    def __init__(self, n):
        """
        Initialize the TwoStack object.
        n: total capacity for both stacks combined
        """
        self.capacity = n
        self.data = [None] * n
        self.left_top = -1
        self.right_top = n

    # ---------------- Left Stack Methods ----------------

    def push_left(self, item):
        if self.left_top + 1 == self.right_top:
            print("Stack Overflow: Cannot push to left stack.")
            return

        self.left_top += 1
        self.data[self.left_top] = item

    def pop_left(self):
        if self.left_top == -1:
            print("Stack Underflow: Left stack is empty.")
            return None

        item = self.data[self.left_top]
        self.data[self.left_top] = None
        self.left_top -= 1
        return item

    def len_left(self):
        return self.left_top + 1

    # ---------------- Right Stack Methods ----------------

    def push_right(self, item):
        if self.right_top - 1 == self.left_top:
            print("Stack Overflow: Cannot push to right stack.")
            return

        self.right_top -= 1
        self.data[self.right_top] = item

    def pop_right(self):
        if self.right_top == self.capacity:
            print("Stack Underflow: Right stack is empty.")
            return None

        item = self.data[self.right_top]
        self.data[self.right_top] = None
        self.right_top += 1
        return item

    def len_right(self):
        return self.capacity - self.right_top

    # ---------------- Transfer Methods ----------------

    def transfer_to_left(self, n):
        if n > self.len_right():
            print("Transfer Error: Not enough items in right stack.")
            return

        for _ in range(n):
            if self.left_top + 1 == self.right_top:
                print("Transfer stopped: Stack Overflow.")
                return
            self.push_left(self.pop_right())

    def transfer_to_right(self, n):
        if n > self.len_left():
            print("Transfer Error: Not enough items in left stack.")
            return

        for _ in range(n):
            if self.left_top + 1 == self.right_top:
                print("Transfer stopped: Stack Overflow.")
                return
            self.push_right(self.pop_left())


# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    print("=== Two Stacks in a List Demo ===")

    stacks = TwoStack(10)

    print("\nPushing to left stack:")
    stacks.push_left(1)
    stacks.push_left(2)
    stacks.push_left(3)

    print("\nPushing to right stack:")
    stacks.push_right(100)
    stacks.push_right(200)
    stacks.push_right(300)

    print("\nLeft stack length:", stacks.len_left())
    print("Right stack length:", stacks.len_right())

    print("\nPop from left stack:", stacks.pop_left())
    print("Pop from right stack:", stacks.pop_right())

    print("\nTransfer 2 items from right stack to left stack")
    stacks.transfer_to_left(2)

    print("Left stack length after transfer:", stacks.len_left())
    print("Right stack length after transfer:", stacks.len_right())

    print("\nTransfer 1 item from left stack to right stack")
    stacks.transfer_to_right(1)

    print("Left stack length after transfer:", stacks.len_left())
    print("Right stack length after transfer:", stacks.len_right())

    print("\nFinal internal array state:")
    print(stacks.data)
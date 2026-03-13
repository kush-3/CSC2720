# kush patel
# homework 1 task 4:

# initialize the node class for the circular linked list
class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.next = None


# initialize the circular linked list class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # append a new node to the circular linked list
    def append(self, pid, burst_time):
        new_node = Node(pid, burst_time)

        # if there is no head then create a new node and make it point to itself
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        # traverse the circular linked list to find the correct position to insert the new node
        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    # remove a node from the circular linked list
    def remove(self, prev, curr):
        # if there is only one node then set the head to None
        if curr == curr.next:
            self.head = None
            return None

        # remove the node from the circular linked list
        prev.next = curr.next

        if curr == self.head:
            self.head = curr.next

        return curr.next

    # check if the circular linked list is empty
    def is_empty(self):
        return self.head is None

    def display(self):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        while True:
            print(f"Process {curr.pid}: Remaining Burst Time = {curr.burst_time}")
            curr = curr.next
            if curr == self.head:
                break

# round robin scheduling algorithm
def round_robin(cll, quantum):
    time = 0

    # check if the circular linked list is empty
    if cll.is_empty():
        return

    # initialize the current node and previous node
    curr = cll.head
    prev = None

    print("\nStarting Round Robin Scheduling:\n")

    # while the circular linked list is not empty
    while not cll.is_empty():
        if prev is None:
            prev = curr
            while prev.next != curr:
                prev = prev.next

        print(f"Time: {time}, Processing PID: {curr.pid}")

        if curr.burst_time > quantum:
            curr.burst_time -= quantum
            time += quantum
            print(f"Process {curr.pid} now has {curr.burst_time} units remaining.\n")

            prev = curr
            curr = curr.next
        else:
            time += curr.burst_time
            print(f"Process {curr.pid} completed.\n")

            curr = cll.remove(prev, curr)

            if cll.is_empty():
                break

            if curr == cll.head:
                prev = None

    print("All processes completed.")
    print(f"Total time taken: {time}")


# driver code:  

if __name__ == "__main__":
    processes = [(1, 10), (2, 5), (3, 8)]
    # initialize the quantum
    quantum = 4

    cll = CircularLinkedList()

    for pid, bt in processes:
        cll.append(pid, bt)

    print("Processes in the list:")
    cll.display()

    round_robin(cll, quantum)
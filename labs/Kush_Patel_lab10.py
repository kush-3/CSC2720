import heapq


class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def add_task(self, task_name, priority_level):
        heapq.heappush(self.heap, (-priority_level, self.counter, task_name))
        self.counter += 1

    def get_most_urgent_task(self):
        if not self.heap:
            return None
        return self.heap[0][2]

    def finish_most_urgent_task(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[2]

    def get_next_n_tasks(self, n):
        sorted_tasks = sorted(self.heap)
        return [task[2] for task in sorted_tasks[:n]]

    def get_last_n_tasks(self, n):
        sorted_tasks = sorted(self.heap, reverse=True)
        return [task[2] for task in sorted_tasks[:n]]

    def change_priority(self, task_name, new_priority):
        self.heap = [
            entry for entry in self.heap if entry[2] != task_name
        ]
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, (-new_priority, self.counter, task_name))
        self.counter += 1


if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.add_task("Write report", 3)
    scheduler.add_task("Fix bug", 5)
    scheduler.add_task("Email client", 1)
    scheduler.add_task("Code review", 4)
    scheduler.add_task("Update docs", 2)

    print("Most urgent task:", scheduler.get_most_urgent_task())

    print("Finish most urgent:", scheduler.finish_most_urgent_task())
    print("Most urgent after finishing:", scheduler.get_most_urgent_task())

    print("Next 3 tasks:", scheduler.get_next_n_tasks(3))

    print("Last 2 tasks:", scheduler.get_last_n_tasks(2))

    scheduler.change_priority("Email client", 10)
    print("Most urgent after priority change:", scheduler.get_most_urgent_task())

    print("\nAll tasks in priority order:")
    while scheduler.get_most_urgent_task():
        print(" ", scheduler.finish_most_urgent_task())

"""Max-heap priority queue and simple task scheduler for Assignment 4."""


class Task:
    def __init__(self, task_id, priority, arrival_time=0, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return (
            f"Task(id={self.task_id}, priority={self.priority}, "
            f"arrival={self.arrival_time}, deadline={self.deadline})"
        )


class PriorityQueue:
    """Priority queue implemented as a max heap."""

    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        maximum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return maximum

    def increase_key(self, task_id, new_priority):
        index = self._find_task(task_id)
        if index == -1:
            raise ValueError("Task not found.")

        if new_priority < self.heap[index].priority:
            raise ValueError("New priority must be greater than or equal to current priority.")

        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def decrease_key(self, task_id, new_priority):
        index = self._find_task(task_id)
        if index == -1:
            raise ValueError("Task not found.")

        if new_priority > self.heap[index].priority:
            raise ValueError("New priority must be less than or equal to current priority.")

        self.heap[index].priority = new_priority
        self._heapify_down(index)

    def _find_task(self, task_id):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                return i
        return -1

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].priority >= self.heap[index].priority:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


def run_scheduler():
    queue = PriorityQueue()

    queue.insert(Task("T1", 3, 0, 10))
    queue.insert(Task("T2", 5, 1, 8))
    queue.insert(Task("T3", 2, 2, 12))
    queue.insert(Task("T4", 4, 3, 9))

    print("Tasks processed from highest to lowest priority:")
    while not queue.is_empty():
        print(queue.extract_max())


if __name__ == "__main__":
    run_scheduler()

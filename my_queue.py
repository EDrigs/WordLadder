class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

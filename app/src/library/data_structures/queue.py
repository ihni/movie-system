class Queue:
    def __init__(self, max_size = 100):
        self.queue = []
        self.max_size = max_size
    
    def is_empty(self):
        if not self.queue:
            return True
        return False

    def is_full(self):
        if len(self.queue) > self.max_size:
            return True
        return False

    def size(self):
        return len(self.queue) 

    def enqueue(self, element):
        if self.is_full(self):
            return "Overflow Error"
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            return "Underflow Error"
        self.queue.pop(0)
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def rotate(self):
        self.enqueue(self.dequeue())
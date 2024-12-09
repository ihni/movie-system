class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''
    Insertions
        - insert_to_beginning(data)
        - insert_to_end(data)
        - insert_at_index(data, idx)

    Updates
        - update_node(data, idx)

    Deletions
        - remove_first()
        - remove_last()
        - remove_at_index(idx)

    Display
        - __str__ and __iter__

    '''
    def __init__(self):
        self.head = None

    def insert_to_beginning(self, data):
        node: object = Node(data)
        node.next = self.head
        self.head = node

    def insert_to_end(self, data):
        node: object = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def insert_at_index(self, data, idx):
        if idx == 0:
            self.insert_to_beginning(data)
            return
        
        position = 0
        current = self.head

        while current and position < idx - 1:
            position += 1
            current = current.next

        if current: # if we found a node at the index
            node = Node(data)
            node.next = current.next
            current.next = node
        else:
            print("Index out of range")

    def update_node(self, data, idx):
        current = self.head
        position = 0
        while current and position < idx:
            if position == idx:
                current.data = data
                return
            position += 1
            current = current.next
        print("Index out of range")

    def remove_first(self):
        if not self.head:
            return
        
        self.head = self.head.next

    def remove_last(self):
        if self.head is None: # if empty
            return
        if not self.head.next: # only one element
            self.head = None
            return
        
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def remove_at_index(self, idx):
        if not self.head:
            return

        current = self.head
        position = 0

        if idx == 0:
            self.remove_first()
            return
        while current and position < idx - 1:
            position += 1
            current = current.next

        if current and current.next:
            current.next = current.next.next
        else:
            print("Index out of range")

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self):
        return " -> ".join(str(item) for item in self)
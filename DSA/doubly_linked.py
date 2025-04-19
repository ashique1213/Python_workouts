class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinked:
    def __init__(self):
        self.head = None
    
    def inser_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    
        
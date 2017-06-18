class MyNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, value):
        new_node = MyNode(value)
        new_node.next_node = self.tail
        self.tail.previous_node = new_node
        self.tail = new_node
    def dequeue(self):
        new_head = self.head.previous_node
        new_head.next_node = None
        self.head = new_head
queue = MyQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.dequeue())
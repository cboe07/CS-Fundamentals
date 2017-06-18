class MyNode:
    def __init__(self, value):
        self.value = value
        self.below_node = None
        self.above_node = None
class MyQueue:
    def __init__(self):
        self.top = None
        self.bottom = None
    
    def push(self,value):
        new_node = MyNode(value)

        self.top.above_node = new_node
        new_node.below_node = self.top

        self.top = new_node

    def pop(self):
        new_top = self.top.below_node
        new_top.above_node = None
        self.top = new_top






    
queue = MyQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.dequeue())



# PUSH
# 1. Instantiate top + new new_node
# 2. Link top + new new_node
# 3. Assign new top

# POP









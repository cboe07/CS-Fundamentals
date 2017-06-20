class MyNode:
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = MyNode(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node

    def remove(self, value):
        current_node = self.head

        while(current_node.value != value and current_node != None):
            current_node = current_node.next_node

        if current_node == None:
            return False

        next_node = current_node.next_node
        previous_node = current_node.previous_node
        next_node.previous_node = previous_node
        previous_node.next_node = next_node
        return True

    def insert(self, value, index):
        new_node = MyNode(value)
        i = 0
        current_node = self.head

        while(i != index - 1 and current_node != None):
            current_node = current_node.next_node
            i += 1

        if current_node == None:
            return self.append(value)

        next_node = current_node.next_node
        next_node.previous_node = new_node
        current_node.next_node = new_node
        new_node.next_node = next_node
        new_node.previous_node = current_node

    def exists(self, value):
        current_node = self.head

        while(current_node.value != value and current_node != None):
            current_node = current_node.next_node

        if current_node == None:
            return False

        return True


class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def my_hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        # Step 1: Figure out what bucket we want to insert the value 
        bucket_index = self.my_hash(value)

         # Step 2: Create the LinkedList if one doesn't exist
        if self.buckets[bucket_index] == None:
            new_linked_list = MyLinkedList()
            self.buckets[bucket_index] = new_linked_list

        # Step 3: Append value to appropriate LinkedList
        self.buckets[bucket_index].append(value)

        
    def exists(self, value):
        # Step 1: Find the bucket we want to look in
        bucket_index = self.my_hash(value)
        # Step 2: If the linkedList doesn't exist at that bucket index, return false
        if self.buckets[bucket_index] == None:
            return False
        # Step 3: Ask the linkedList if the value exists
        return self.buckets[bucket_index].exists(value)
        



hash_table = MyHashTable()
hash_table.insert('Hello World')
hash_table.insert('Bob')
hash_table.insert('Cathy')
hash_table.insert('Zebra')

print(hash_table.exists('Hello World'))


print(hash_table.buckets)

















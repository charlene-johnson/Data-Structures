"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when implementing a Stack?
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # return all values in list
    def __str__(self):
        # output set to None
        output = ''

        # setting current node to the head
        current_node = self.head

        # looping through current node until None
        while current_node is not None:

            # this will output all values within current node
            output += f'{current_node.value} -> '

            # moving current node to next node
            current_node = current_node.next_node

        # returning the output
        return output

    # add to head
    def add_to_head(self, value):
        # create node
        new_node = Node(value)

        # sanity check
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # setting new node to head (moving)
            new_node.next_node = self.head
            self.head = new_node

    # add to tail
    def add_to_tail(self, value):
        # create node
        new_node = Node(value)

        # sanity check
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # setting new node to tail(moving)
            self.tail.next_node = new_node
            self.tail = new_node

    # remove head and return the value
    def remove_head(self):
        # if empty, do nothing
        if not self.head:
            return None
        # returning 1 element set head/tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False

# implement class Stack for linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        node = self.storage.remove_head()
        return node


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         self.size -= 1
#         node = self.storage.pop(0)
#         return node


new_stack = Stack()
print(len(new_stack))
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
new_stack.push(6)
print(len(new_stack))
print(new_stack.storage)
print(f'removed value is {new_stack}')

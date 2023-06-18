class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__ (self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


def append(self,value):
    new_Node = Node(value)
    if self.head is None:
      self.head = new_Node
      self.tail = new_Node
    else:
      self.tail.next = new_Node
      self.tail= new_Node
    self.length += 1
    return True


def print_list(self, value):
   temp = self.head
   while temp is not None:
      print(temp.value)
      temp = temp.next



    

my_linked_list = Linkedlist(3)

print('head:', my_linked_list.head.value)
print('tail:', my_linked_list.tail.value)
print('length:', my_linked_list.length)



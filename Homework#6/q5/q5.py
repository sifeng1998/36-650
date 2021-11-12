class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node
    
    # Remove duplicates from Singly Linked List
    def remove_dups(self):
        tmp = self.head
        # create a list to store values
        new_list = []
        # create a pointer to help keep track of comparing the value
        iterate = None
        # edge case for length 0 and 1: no duplicates
        if self.head is None or self.head.next is None:
            return

        while tmp:
            if tmp.data not in new_list:
                # append value to new list
                new_list.append(tmp.data)
                # then iterate refers to the one just added in list and tmp moves to the next one
                iterate = tmp
                tmp = tmp.next
            else:
                # no append value to new list
                # skip this one and both iterate and tmp move to the next one
                iterate.next = tmp.next
                tmp = tmp.next
        return self

# test case
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)

print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the Linked List is:")
linked_list.print_list()

# test case
first_node = Node(20)
linked_list = LinkedList(first_node)
linked_list.insert(4)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(1)

print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing the duplications, the Linked List is:")
linked_list.print_list()
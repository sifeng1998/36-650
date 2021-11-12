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
    
    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size
    
    # Sort the unsorted linked list in ascending order
    def sort(self):
        # create a pointer pointing to the head
        tmp = self.head
        # Selection Sort
        # Traverse through all linked list elements
        while tmp:
            # Find the minimum element in remaining 
            # unsorted linked list
            min_idx = tmp
            next_idx = tmp.next
            
            while next_idx:
                if next_idx.data < min_idx.data:
                    min_idx = next_idx
                next_idx = next_idx.next
                
            # Swap the found minimum element with
            # the first element 
            iterate = tmp.data
            tmp.data = min_idx.data
            min_idx.data = iterate
            tmp = tmp.next
                        

# test case
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
print("The Linked List is:")
linked_list.print_list()

linked_list.sort()
print("After sorting, the Linked List is:")
linked_list.print_list()

# test case
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(9)
linked_list.insert(7)
linked_list.insert(11)
linked_list.insert(2)
linked_list.insert(9)
print("The Linked List is:")
linked_list.print_list()

linked_list.sort()
print("After sorting, the Linked List is:")
linked_list.print_list()
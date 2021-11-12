class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Reverse Linked List
class ReversedLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    # Insert a node in a linked list - Create the Insert Function
    def insert(self, data):
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            while (current.previous):
                current = current.previous
            current.previous = node
    # Insert a node in a reversed linked list
    def insert(self, data):
        node = Node(data)
        node.previous = self.tail
        self.tail = node

    # Delete a node in a linked list - Create the Delete Function
    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        # Check if tail node is to be deleted
        if self.tail.data == data:
            self.tail = temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return
    
    # Create the Search Function
    def search(self,data):
        current = self.tail
        while current:
            if current.data == data:
                return True
            else:
                current = current.previous
        
        return False

# test case
first_node = Node(11)
linked_list = ReversedLinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The Reversed Linked List is (after insertion):")
linked_list.print_list()

linked_list.delete(6)
print("The Reversed Linked List is (after deleting 6):")
linked_list.print_list()

print("Does 5 exist in the Reversed Linked List?")
print(linked_list.search(5))

print("Does 17 exist in the Reversed Linked List?")
print(linked_list.search(17))
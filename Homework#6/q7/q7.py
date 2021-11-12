# Create the data structure 
class Node:
    def __init__(self, data):
        self.tooBig = None # Too-big children
        self.big = None # Big children
        self.small = None # Samll children
        self.data = data # Node data
    
    # Create the insert function 
    def insert(self, data):
        if self.data:
            # consider the case for too-big children
            if data - self.data >=10:
                if self.tooBig:
                    self.tooBig.insert(data)
                else:
                    self.tooBig = Node(data)
                # consider the case for big children
            elif (data - self.data >= 0) and (data - self.data < 10):
                if self.big:
                    self.big.insert(data)
                else:
                    self.big = Node(data)
                # consider the case for small children
            else:
                if self.small:
                    self.small.insert(data)
                else:
                    self.small = Node(data)
        else: 
            self.data = data
    
    # Create the delete function
    def delete(self, data):
        new_list = []
        # traverse the elements in the current tree
        self.traversal_list(new_list)
        # set the previous data to be null and readd elements to a new list
        self.readd_list()
        # insert elements in the new tree using for loop
        for node in new_list:
            if node == data:
                continue
            if not self.data:
                self.data = node
            else:
                self.insert(node)
    
    def traversal_list(self, answer = None):
        # create a list for traversal elements
        if self.small:
            self.small.traversal_list(answer)
        if answer is not None:
            answer.append(self.data)
        if self.big:
            self.big.traversal_list(answer)
        if self.tooBig:
            self.tooBig.traversal_list(answer)

    # set the previous data to be null
    def readd_list(self):
        self.tooBig = None
        self.big = None
        self.small = None
        self.data = None
        return self

    # Create the traversal function
    def traversal(self):
        # start with the small child
        if self.small:
            self.small.traversal()
        print(self.data)
        # follow by the big child
        if self.big: 
            self.big.traversal()
        # follow by the too-big child
        if self.tooBig:
            self.tooBig.traversal()        

# test case
root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)
root.insert(19)

print("Tree contents after insertion using the traversal():")
root.traversal()

root.delete(45)

print("Tree contents after deleting 45 using the traversal():")

root.traversal()
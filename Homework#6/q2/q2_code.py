class Queue:
    inner_list = []
    top = 0
    
    def enqueue(self,value):
        self.inner_list.insert(self.top,value)
        self.top = self.top + 1 
    
    def dequeue(self):
        value = self.inner_list.pop(0)
        return value
    
    def delete(self, point):         
        for i in range(len(self.inner_list)):
            # pop up every element from the queue
            tmp = self.dequeue()
            # if the pop-up element does not match to the one we want to delete
            # put it back to the queue
            if tmp != point:
                self.enqueue(tmp)
        return self

# test case
obj = Queue ()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

obj.delete(7)
print(obj.dequeue())
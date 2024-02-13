class Ticket:
    def __init__(self):
        self.queue = []
        
    def get_queue(self):
        return self.queue
    
    def is_empty(self):
        return len(self.queue) == 0    
    
    def enqueue(self, item):
         self.queue.append(item)
         
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        

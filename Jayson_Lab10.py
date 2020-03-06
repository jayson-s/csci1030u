#Name: Jayson Sandhu
#Student ID: 100659589

class Queue:
    def __init__(self):
        self.front = 0
        self.data = []

    def enqueue(self,value):
        if(len(self.data) == 0):
            self.front = 0
        self.data.append(value)
    def dequeue(self):
        if(len(self.data) == 0):
            return "Error: No such element in queue"
        else:
            dataToReturn = self.data[0]
            self.data.pop(0)
            return dataToReturn
}			

queue = Queue()
print('isEmpty():', queue.isEmpty())
print('empty:', queue)
queue.enqueue(10)
print('after enqueue(10):', queue)
print('isEmpty():', queue.isEmpty())
queue.enqueue(1)
print('after enqueue(1):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
queue.enqueue(2)
print('after enqueue(2):', queue)
queue.enqueue(3)
print('after enqueue(3):', queue)
queue.enqueue(4)
print('after enqueue(4):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
1
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('isEmpty():', queue.isEmpty())


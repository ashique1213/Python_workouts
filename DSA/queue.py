class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if not self.dequeue:
            print("Empty")
            return
        self.queue.pop(0)

    def peek(self):
        if not self.dequeue:
            print("Empty")
            return
        print(self.queue[0])
    

    def reverse(self):
        if not self.queue:
            return
        front = self.queue.pop(0)
        self.reverse()
        self.enqueue(front)

    def isEmpty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)


que = Queue()
que.enqueue(13)
que.enqueue(12)
que.enqueue(16)
que.enqueue(19)
que.display()
que.dequeue()
que.display()
que.peek()
que.reverse()
que.display()

# circular queue

class CircularQueue:
    def __init__(self,capacity):
        self.front = 0
        self.rear = -1
        self.capacity = capacity
        self.queue= [None]*capacity

    def enqueue(self,data):
        if self.rear == self.capacity-1:
            print('full')
            return
        self.rear+=1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front > self.rear:
            print("empty")
            return
        for i in range(self.rear):
            self.queue[i]=self.queue[i+1]
        
        self.rear-=1
    
    def display(self):
        if self.front > self.rear:
            print('empty')
            return
        for i in range(self.front,self.rear):
            print(self.queue[i],end='<--')

q = CircularQueue(4)

q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.dequeue()
q.display()


class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert 
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("penuh!!\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete 
    def dequeue(self):
        if (self.head == -1):
            print("kosong!!\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def display(self):
        if(self.head == -1):
            print("No element!!")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()



circularQueue = MyCircularQueue(5) 
circularQueue.enqueue (14) 
circularQueue.enqueue (22) 
circularQueue.enqueue (13) 
circularQueue.enqueue (-6) 
circularQueue.display() 
print ("Data yang dihapus adalah = ", circularQueue.dequeue()) 
print ("Data yang dihapus adalah = ", circularQueue.dequeue()) 
circularQueue.display() 
circularQueue.enqueue (9) 
circularQueue.enqueue (20) 
circularQueue.enqueue (5) 
circularQueue.display()




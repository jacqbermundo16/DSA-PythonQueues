from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

#adding and printing the elements
print()
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())
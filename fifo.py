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

#printing the length of the elements enqueued
fifo = Queue("1st", "2nd", "3rd")
print(len(fifo))
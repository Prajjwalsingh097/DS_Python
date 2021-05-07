# Imprting deque class from collections 
from collections import deque
import time
import threading

class queue:
    que=[]
    # Initialize the list with associate with deque class
    def __init__(self):
        self.que=deque()

    # Methods like endueue and dequeue 
    def enqueue(self,data):
        # it will store data always in 0th position 
        self.que.appendleft(data)

    def dequeue(self):
        # pop method get data from last index
        # as data inserted also get deleted
        if len(self.que)==0:
            return "\n\t Queue is empty"

        return self.que.pop()

    def isEmpty(self):
        # it will retuen boolean True if length is 0 else false 
        return len(self.que)==0

    def size(self):
        # Normal method returns len 
        return len(self.que)


'''
q=queue()

q.enqueue(['prajjwal','singh'])
q.enqueue(['prajjwal','singh'])
q.enqueue(['prajjwal','singh'])
q.enqueue(['prajjwal','singh'])
print(q.que)


'''


food =queue()

def orderFood(orders):
    for x in orders:
        food.enqueue(x)
        print("\n\t Order for : ",x)
        time.sleep(0.5)

def server():
    time.sleep(1)
    while food.isEmpty()==False:
        print("\n\t Food Servered",food.dequeue())
        time.sleep(2)

    print("----Servered---")


orders=['Pizza','Garlic Bread','Paneer Pakoda']

t1=threading.Thread(target = orderFood, args=(orders,))
t2=threading.Thread(target = server)



t1.start()
t2.start()





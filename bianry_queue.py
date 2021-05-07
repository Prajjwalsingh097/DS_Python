from collections import deque

class queue:
    que=[]
    def __init__(self):
        self.que=deque()

    def enqueue(self,data):
        self.que.appendleft(data)
        
    def dequeue(self):
        if len(self.que)==0:
            return "\n\t Queue is empty"
        else:
            return self.que.pop()

    def isEmpty(self):
        return len(self.que)==0

    def size(self):
        return len(self.que)
    

q=queue()

for x in range(1,11):
    s=""
    while x>=1:
        s=str(x%2)+s
        x=x//2
    q.enqueue(s)

print(q.que)


while q.isEmpty()==False:
    print(q.dequeue())
    

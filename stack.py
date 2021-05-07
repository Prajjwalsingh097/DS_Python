from queue import deque


#implement a stack using deque and list
class stack:
    container=[]

    
    def _init__(self):
        self.container=deque()

    def push(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def print(self):
        print(self.container[::-1])
    


s=stack()

s.push(20)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
s.push('Prajjwal')
print(s.peek())
#s.pop()
s.print()

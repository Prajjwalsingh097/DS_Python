class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def inserBeg(self,data):
        node=Node(data,self.head)
        self.head=node

    def printData(self):
        if self.head is None:
            print("Empty Link List")
            return
        itr=self.head
        linkstr=""
        while itr:
            linkstr += str(itr.data)+'-->'
            itr=itr.next
        print(linkstr)
        
    def insertEnd(self,data):
        if self.head is None:
            self.head=Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insertValues(self, data_list):
        #self.head=None
        for data in data_list:
            self.insertEnd(data)
        
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            itr= itr.next
            #print(itr)
            count+=1
        return count

    def removeAt(self, index):
        if index<0 or index>self.getLength():
            raise Exception("Invalid index")

        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            
            if count==(index-1):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insertAt(self,index,data):
        if index<0 or index>self.getLength():
            raise Exception("Invalid index")

        if index==0:
            self.inserBeg(data)
            return
        
        count=0
        itr=self.head
        while itr:
            print(itr.data)
            if count==(index-1):
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def getData(self):

        itr=self.head
        while itr:
            print(itr.data)
            itr=itr.next

    def insertAfterValue(self,value,data):

        itr=self.head
        while itr:
            if itr.data==value:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next

            
    def removeByValue(self,value):

        itr=self.head
        while itr:
            
            if itr.data==value:
                itr.next=itr.next.next
                break
            itr=itr.next

            
            
                


ll=linkedlist()
ll.inserBeg(56)

ll.insertValues(['Riya','Sotu',1,'Prajjwal'])

#print("\n\t Head Value :",(ll.head.next.data))
print("\n\n Printer After Complete Filling :- ")
ll.printData()


ll.insertAfterValue(56,57)
print("\n\n Printer After Inserting 57 after 56 :- ")
ll.printData()

ll.removeByValue(56)
print("\n\n Printer After Remove 56 :- ")
ll.printData()


'''

ll.inserBeg(6)
ll.inserBeg(16)
#ll.insertEnd(100)
#ll.insertValues(['Riya','Sotu',1,'Prajjwal'])



sys.exit()

'''

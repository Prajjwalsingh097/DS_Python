class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    # Adding Cjild nodes 
    def addChild(self,data):
        if self.data==data:
            print("\nValue ",data," Already Exist")
            return

        if self.data>data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinaryTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinaryTree(data)

    def search(self,data):

        if self.data==data:
            print("Value Exist ",data)
            return True

        if self.data>data:
            # After Checking is searching data smaller then Root one
            # We check is there is any node exist in left side or not
            
            if self.left:
                return self.left.search(data)
            else:
                print("Value Not Exist")
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                print("Value Not Exist")
                return False

    def getLeftMostSmallest(self):

        if self.left:
            return self.left.getLeftMostSmallest()
        else:
            #print(self.data)
            return self.data
            
    def getRightMostBiggest(self):

        if self.right:
            return self.right.getRightMostBiggest()
        else:
            return self.data

            
        

    def InOrderTraversal(self):
        # the output list we are going to return as O/P
        element=[]

        # Visit left or left of left.....Upto Last Left Leaf 
        if self.left:
            element+= self.left.InOrderTraversal()

        # Bit Confusing But its working
        # Where the data is coming 
        element.append(self.data)

        # Visiting the Right Node >> And there "Left Node Right"
        if self.right:
            element+= self.right.InOrderTraversal()
            
        
        return element

    def delete(self,val):

        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.right
            if self.left is None:
                return self.right

            len_right=len(self.right.InOrderTravsal())
            len_left=len(self.left.InOrderTravsal())

            if len_right>len_left:
                minVal=self.right.getLeftMostSmallest()
                self.data=minVal
                self.right= self.right.delete(minVal)
            else:
                minVal=self.left.getRightMostBiggest()
                self.data=minVal
                self.left= self.left.delete(minVal)
           
                

        return self.data

    def printTree(self):

        #print("\n\t Root is ",self.data)
        if self.left:
            print("\n\t Left of ",self.data,self.left.printTree())
        if self.right:
            print("\n\t Right of ",self.data,self.right.printTree())

        if self.left is None and self.right is None:
            return self.data
            
        return self.data

BinaryListInput=[4,2,5,7,1,9,1,2]

print("\n\n\t Binery Tree Opeartions on List Elements \n\t Input List ",BinaryListInput)

b=BinaryTree(BinaryListInput[0])




for x in range(1,len(BinaryListInput)):
    b.addChild(BinaryListInput[x])



add =b.InOrderTraversal()
print("\n\n\t In Order Traversal (LNR) : ",add)
ad=0
for x in add:
    ad=ad+x

print("\n\n\t  Addition Of all the elemts are ",ad)

print("\n\n\t Most Left(Smallest) : ",b.getLeftMostSmallest())
print("\n\n\t Most Right(Biggest) : ",b.getRightMostBiggest())



print("\n\n\t Deleting 5 ",b.delete(5))

add =b.InOrderTraversal()
print("\n\n\t In Order Traversal (LNR) : ",add)

root=b.printTree()
print("\n\n\n\t\t Binary Tree \n\t Root ",root)
print("\n\n\t ",b.printTree())


'''


print("\n\n\t Binary Tree Operation in county(String data)")
cntry=["india","china","pakistan","usa"]

cnt=BinaryTree(cntry[0])

for x in range(1,len(cntry)):
    cnt.addChild(cntry[x])

print(cnt.InOrderTraversal())

'''





    

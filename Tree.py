class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)
        
    def getLevel(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
        
    def getData(self):
        space=""
        print(self.getLevel())
        if self.getLevel()>0:
            space=(self.getLevel()*" ")+"|"+(self.getLevel()*"-")
        print(space+self.data)
        # First it will check for the Children (Is there any children or not)
        if self.children:
            for child in self.children:
                child.getData()
        
    def getDataThruLevel(self,level):
        
        lev=self.getLevel()
        
        while level>=lev:
            space=""
            if self.getLevel()>0:
                space=(self.getLevel()*" ")+"|"+(self.getLevel()*"-")
            print(space+self.data)
            
            # First it will check for the Children (Is there any children or not)
            if self.children:
                for child in self.children:
                    child.getDataThruLevel(level)
            break



# Making a root Node "Names Electronics"
root=Tree('Electronics')

# Making a new node Laptop (After that make it chil for Root
lappy=Tree("Laptop")

# Adding Child of Laptop Node 
lappy.addChild(Tree("HP"))
lappy.addChild(Tree("Dell"))
lappy.addChild(Tree("Lenovo"))

# Now the time to add Laptop(Lappy) Node to the child node or root node
root.addChild(lappy)

# Now Doing the same with two more nodes and there child and add the that node to root's Child Node

TV=Tree("TV")
TV.addChild(Tree("LG"))
TV.addChild(Tree("SAMSUNG"))
root.addChild(TV)


root.getData()

# We are going to make a tree with level Based Structure

print("\n\n\t Printing data Through Level ")

root.getDataThruLevel(1)


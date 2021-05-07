# Graph Normal Graph Data Structure

class Graph:
    def __init__(self, edges):

        self.edge=edges
        self.dict={}
        for start, end in self.edge:

            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start]=[end]

        print(self.dict)

    def getRoute(self, start, end, path=[]):
        path=path+[start]
        if start==end:
            return [path]

        if start not in self.dict:
            print("Not in Keys")
            return None

        shortestPath=None
        for node in self.dict[start]:
            if node not in path:
                sp=self.getRoute(node,end,path)
                if sp:
                    if shortestPath is None or len(sp)<len(shortestPath):
                        shortestPath=sp


        return shortestPath
        
            

        
        


dict={
    ('Mumbai','Paris'),
    ('Mumbai','Dubai'),
    ('Dubai','USA'),
    ('Paris','Dubai'),
    ('Paris','USA'),
    ('USA','Toranto')
    
    }

RouteOfGraph=Graph(dict)

start='Mumbai'
end='Paris'
print(f"Shortest Path {start}, to {end}",RouteOfGraph.getRoute(start,end))








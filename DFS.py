from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def DFS(self, visited, v):
        visited[v] = True
        print(v, end=' ')
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(visited, i)
                
    def DFS_main(self, u):
        visited = [False] * (len(self.graph))
        print(visited)
        print("The DFS order will be : \n")
        self.DFS(visited, u)

g = Graph()
i=0
while i==0:
    print("do you want to add edge if yes hit 'y' \n")
    s = input()
    if s=='y':
        u,v  = map(int,input("Enter a first and second node: ").split())
        print(u,v, type(u))
        g.addEdge(u,v)
    else:
        i=1
print(g.graph)
print("Please enter starting node : ")
u = int(input())
print("\nstarting vertex : ", u)
g.DFS_main(u)

        
    
            
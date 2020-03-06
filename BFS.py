from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self, visited, v):
        
        queue = []
        bfs = []
        queue.append(v)
        
        while queue:
            print("Queue : ",queue)
            s = queue.pop(0)
            visited[s] = True
            bfs.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    if (i not in queue):
                        queue.append(i)
            print("BFS order will be : ",bfs)
                
                
    def BFS_main(self, u):
        visited = [False] * (len(self.graph))
        print(visited)
        print("The BFS order will be : \n")
        self.BFS(visited, u)

g = Graph()
i=0
while i==0:
    print("do you want to add edge if yes hit 'y' \n")
    s = input()
    if s=='y':
        u,v  = map(int,input("Enter a first and second node: ").split())
        #print(u,v)
        g.addEdge(u,v)
    else:
        i=1
print(g.graph)
print("Please enter starting node : ")
u = int(input())
print("\nstarting vertex : ", u)
g.BFS_main(u)

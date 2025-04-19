from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self,vertex):
        self.adj_list[vertex]= []
    
    def add_edges(self,vertex1,vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:

            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
    
    def bfs(self,start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
                queue.extend(self.adj_list[vertex])

    def dfs(self,start,visited = None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start,end=' ')
        for n in self.adj_list[start]:
            if n not in visited:
                self.dfs(n,visited)


    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}->{self.adj_list[vertex]}")


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edges('A', 'B')
g.add_edges('A', 'C')
g.add_edges('D', 'E')
g.display()
# g.bfs('A')
# g.dfs('D')
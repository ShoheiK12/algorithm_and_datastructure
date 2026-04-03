# Graph implementation using Adjacency Matrix
# Undirected graph, with weighted or unweighted edges

class Vertex:
  def __init__(self, n):
    self.name = n
    
class Graph:
  vertices = {}
  edges = []
  edge_indices = {}
  
  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      self.vertices[vertex.name] = vertex
      # for loop appends a column of zeros to the edges matrix
      for row in self.edges:
        row.append(0)
      # append a row of zeros to the bottom of the edges matrix
      self.edges.append([0] * (len(self.edges) + 1))
      self.edge_indices[vertex.name] = len(self.edge_indices)
      return True
    else:
      return False    
    
  def add_edge(self, u, v, weight=1):
    if u in self.vertices and v in self.vertices:
      self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
      self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
      return True
    else:
      return False
    
  def print_graph(self):
    for v, i in sorted(self.edge_indices.items()):
      print(v + ' ', end='')
      for j in range(len(self.edges)):
        print(self.edges[i][j], end=' ')
      print(' ')
      
# Test code for Vertex and Graph Class
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
  g.add_vertex(Vertex(chr(i)))
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
  g.add_edge(edge[0], edge[1])

g.print_graph()

"""
Output:
A 0 1 0 0 1 0 0 0 0 0  
B 1 0 0 0 0 1 0 0 0 0  
C 0 0 0 0 0 0 1 0 0 0
D 0 0 0 0 1 0 0 1 0 0
E 1 0 0 1 0 0 0 1 0 0
F 0 1 0 0 0 0 1 0 1 1
G 0 0 1 0 0 1 0 0 0 1
H 0 0 0 1 1 0 0 0 1 0
I 0 0 0 0 0 1 0 1 0 0
J 0 0 0 0 0 1 1 0 0 0
"""
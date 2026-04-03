class Vertex:
  """
  Vertex class has a constructor that sets the name of the vertex and creates a new empty set to store neighbours.
  The add_neighbour method adds the name of a neighbouring vertex to the neighbour set. This set automatically eliminates duplicates.
  """
  def __init__(self, n):
    self.name = n
    self.neighbours = set()
    
  def add_neighbour(self, v):
    self.neighbours.add(v)
    
class Graph:
  vertices = {}
  
  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      self.vertices[vertex.name] = vertex
      return True
    else:
      return False
  
  def add_edge(self, u, v):
    if u in self.vertices and v in self.vertices:
      self.vertices[u].add_neighbour(v)
      self.vertices[v].add_neighbour(u)
      return True
    else:
      return False
    
  def print_graph(self):
    for key in sorted(list(self.vertices.keys())):
      print(key, sorted(list(self.vertices[key].neighbours)))
      
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
A ['B', 'E']
B ['A', 'F']
C ['G']
D ['E', 'H']
E ['A', 'D', 'H']
F ['B', 'G', 'I', 'J']
G ['C', 'F', 'J']
H ['D', 'E', 'I']
I ['F', 'H']
J ['F', 'G']
"""
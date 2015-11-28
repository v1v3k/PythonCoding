import sys
class Vertex:

	def __init__(self,node):
		self.adjacent = {}
		self.visited = False
		self.id = node
		self.distance = sys.maxint
		self.previous = None

	def addNeighbour(self,neigh,weight):
		self.adjacent[neigh] = weight

	def getConnections(self):
		return self.adjacent.keys()

	def getVertexId(self):
		return self.id

	def getWeight(self,node):
		return self.adj_list[node]

	def setDistance(self,d):
		self.distance = d

	def setPrevious(self, p):
		self.previous = p

	def setVisited(self):
		self.visited = True

	def getDistance(self,d):
		return self.distance

	def getPrevious(self, p):
		return self.previous

	def getWeight(self,p):
		return self.adjacent[p]

	def __str__(self):
		return str(self.id)+' '+[str(i.id) for i in self.adj_list.keys()]

class Graph:

	def __init__(self):
		self.vertDictionary = {}
		self.no_vertex = 0

	def __iter__(self):
		return iter(self.vertDictionary.values())

	def addVertex(self,n):
		new_vertex = Vertex(n)
		self.vertDictionary[n] = new_vertex
		self.no_vertex += 1
		return new_vertex

	def getVertex(self,n):
		if n in self.vertDictionary:
			return self.vertDictionary[n]
		else:
			return  None

	def addEdge(self,v1,v2,weight):
		if v1 not in self.vertDictionary:
			self.addVertex(v1)

		if v2 not in self.vertDictionary:
			self.addVertex(v2)

		self.vertDictionary[v1].addNeighbour(self.vertDictionary[v2],weight)
		self.vertDictionary[v2].addNeighbour(self.vertDictionary[v1],weight)

	def getVertices(self):
		return  self.vertDictionary.keys()

	def getEdges(self):
		edge_list = []

		for v in self.vertDictionary.values():
			for w in v.adjacent.keys():
				z = ([w.getVertexId() ,v.getVertexId() , v.getWeight(w)])
				if ( z not in edge_list):
					edge_list.append ([v.getVertexId() ,w.getVertexId() , v.getWeight(w)] )
		return edge_list


if __name__ == '__main__':
	print "main"
	G =Graph()
	G.addVertex('a')
	G.addVertex('b')
	G.addVertex('c')
	G.addVertex('d')
	G.addEdge('a','b',4)
	G.addEdge('a','c',14)
	G.addEdge('a','d',2)
	G.addEdge('b','d',3)


	print G.getEdges()
import Core_Ds.Adj_Matrix_Graph as Matrix


if __name__ == '__main__':
    G = Matrix.Graph(5)

    G.setVertex(0,'a')
    G.setVertex(1,'b')
    G.setVertex(2,'c')
    G.setVertex(3,'d')
    G.setVertex(4,'e')

    print 'graph data'

    G.addEdge('a','e',10)
    G.addEdge('a','c',20)
    G.addEdge('c','b',30)
    G.addEdge('b','e',40)
    G.addEdge('e','d',50)
    G.addEdge('f','e',60)


    print G.printMatrix()
    print G.getEdges()


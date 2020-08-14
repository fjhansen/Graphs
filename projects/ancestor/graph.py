"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self._vertices_len = len(self.vertices.values())

    def __len__(self):
        print(self._vertices_len)
        return self._vertices_len

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # the set adds the vertex
        self.vertices[vertex_id] = set()
        print("ADDING_VERTEX: \n",self.vertices)

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        # adds v2 to v1 set
        self.vertices[v1].add(v2)
        
        print('ADDING_EDGE: \n',self.vertices)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # returning edges based on vertex ID
        print("NEIGHBORS: \n",self.vertices[vertex_id])
        return self.vertices[vertex_id]

    def get_all_in_graph(self):
        print('ALL_VERTICES: \n',len(self.vertices.items()))
        return len(self.vertices.items())

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)

        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:

                visited.add(v)
                print(v)

                for neighbor in self.vertices[v]:
                    if neighbor not in visited:
                        q.enqueue(neighbor)
        return visited
    # TODO
    # order: next node to be visited
    # keep the order in a queue
        
##        q = Queue()
##        visited = [False] * len(self.vertices.items())
##        g = self.get_neighbors(starting_vertex)
##        g = list(g)
##        print("G:",type(g))
##        print("VISITED:",visited)
##        q.enqueue(starting_vertex)
##
##        while q:
##            vertex = q.dequeue()
##            if vertex not in visited:
##                visited[vertex] = True
##                print("VIS",visited)
##                neighbors = g[vertex]
##
##            for y in neighbors:
##                if y is False:
##                    q.enqueue(y)
##            
                

    

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    s.push(neighbor)
        return visited
                

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
          # TODO
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
            
                                            # this makes a call to visited set not a copy
                self.dft_recursive(neighbor, visited)
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Queue()

        q.enqueue([starting_vertex])
        

        visited = set()
        print("Q_V: \n",visited)
        
        

        while q.size() > 0:
                  print("Q_TEST: \n",q.queue)
                  current_path = q.dequeue()
                  last_node = current_path[-1]
                  if last_node not in visited:
                      if last_node == destination_vertex:
                          print("Q_P: \n",current_path)
                          return current_path
                      else:
                          visited.add(last_node)
                          neighbors = self.get_neighbors(last_node)
                          for neighbor in neighbors:
                              copy = current_path[:]
                              copy.append(neighbor)
                              q.enqueue(copy)
                  

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            current_path = s.pop()
            last_node = current_path[-1]
            if last_node not in visited:
                if last_node == destination_vertex:
                    return current_path
                else:
                    visited.add(last_node)
                    neighbors = self.get_neighbors(last_node)
                    for neighbor in neighbors:
                        copy = current_path[:]
                        print("DFS_C: \n",copy)
                        copy.append(neighbor)
                        s.push(copy)
                        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex] # this makes a copy of the path

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                
                                                # neighbor becomes new starting_vertex
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None
                    
            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    graph.get_all_in_graph()

##for x in graph.get_neighbors(2):
##    graph.get_neighbors(x)

    #graph.get_neighbors(2)


##    graph.add_edge(1,2)
##    graph.add_edge(2,4)
##    graph.add_edge(2,3)
##    graph.add_edge(2,4)
##    graph.add_edge(3,5)
##    graph.add_edge(4,7)
##    graph.add_edge(4,6)
##    graph.add_edge(5,3)
##    graph.add_edge(6,3)
##    graph.add_edge(7,1)
##    graph.add_edge(7,6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("BFT: \n",graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
##    graph.dft(1)
##    print("DFT: \n", graph.dft(1))
##    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
##    print("DFS: \n",graph.dfs(1, 6))
##    print("DFS_R: \n",graph.dfs_recursive(1, 6))


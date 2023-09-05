# this is adjacency list
from collections import deque


class Graph:
    def __init__(self, V):
        # an array to store all vertex object
        self.vertices = [None] * len(V)
        for index, element in enumerate(V):
            self.vertices[index] = Vertex(element)

        #     lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        #     index   0 ,  1,   2,   3,   4,   5,   6,   7

        """
        BASED ON WEEK 8 LECTURE NOTES PAGE 172
        """
        #  for vertex A
        self.vertices[0].edges.append(Edge(self.vertices[0], self.vertices[2]))
        self.vertices[0].edges.append(Edge(self.vertices[0], self.vertices[1]))

        # for vertex C (since its undirected)
        self.vertices[2].edges.append(Edge(self.vertices[2], self.vertices[0]))
        self.vertices[2].edges.append(Edge(self.vertices[2], self.vertices[3]))

        #  for vertex D
        self.vertices[3].edges.append(Edge(self.vertices[3], self.vertices[2]))

        #  for vertex B
        self.vertices[1].edges.append(Edge(self.vertices[1], self.vertices[0]))
        self.vertices[1].edges.append(Edge(self.vertices[1], self.vertices[5]))
        self.vertices[1].edges.append(Edge(self.vertices[1], self.vertices[4]))

        # for vertex F
        self.vertices[5].edges.append(Edge(self.vertices[5], self.vertices[1]))
        self.vertices[5].edges.append(Edge(self.vertices[5], self.vertices[6]))

        # for vertex E
        self.vertices[4].edges.append(Edge(self.vertices[4], self.vertices[1]))
        self.vertices[4].edges.append(Edge(self.vertices[4], self.vertices[6]))
        self.vertices[4].edges.append(Edge(self.vertices[4], self.vertices[7]))

        # for vertex G
        self.vertices[6].edges.append(Edge(self.vertices[6], self.vertices[5]))
        self.vertices[6].edges.append(Edge(self.vertices[6], self.vertices[4]))
        self.vertices[6].edges.append(Edge(self.vertices[6], self.vertices[7]))

        # for vertex H
        self.vertices[7].edges.append(Edge(self.vertices[7], self.vertices[6]))
        self.vertices[7].edges.append(Edge(self.vertices[7], self.vertices[4]))

    def bfs(self):
        """
        IF THE GRAPH IS UNWEIGHTED, BFS CAN BE USED TO FIND SHORTEST DISTANCE FROM SOURCE TO DESTINATION.
        """
        discovered_lst = deque()
        visited_lst = []
        source = self.vertices[0]

        discovered_lst.append(source)
        source.discovered_vertex()

        while discovered_lst:
            u = discovered_lst.popleft()
            visited_lst.append(u)
            u.visited_vertex()
            for edge in u.edges:
                edge = edge.v
                if edge.discovered == False and edge.visited == False:
                    discovered_lst.append(edge)
                    edge.discovered_vertex()

        return visited_lst

    def dfs(self):
        stack = []
        visited_lst = []
        stack.append(self.vertices[0])

        while stack:
            u = stack.pop()
            visited_lst.append(u)
            u.visited_vertex()
            for edge in u.edges:
                edge = edge.v
                if edge.discovered == False and edge.visited == False:
                    stack.append(edge)
                    edge.discovered_vertex()
        return visited_lst

    def bfs_shortest_path(self):
        """
        FIND THE SHORTEST DISTANCE FROM SOURCE TO ALL VERTICES BASED ON THE MINIMUM NUMBER OF EDGES
        ONLY APPLICABLE IF THE GRAPH IS UNWEIGHTED. IF THE GRAPH IS WEIGHTED (POSITIVE WEIGHT) , THEN
        WE NEED TO USE DIJIKSTRA
        """
        discovered_lst = deque()
        visited_lst = []
        source = self.vertices[0]

        discovered_lst.append([source, source.distance, source.previous])
        source.discovered_vertex()

        while discovered_lst:
            u = discovered_lst.popleft()
            visited_lst.append(u)
            u[0].visited_vertex()
            for edge in u[0].edges:
                v = edge.v
                v.distance = edge.u.distance + 1
                v.previous = edge.u.id

                if v.discovered == False and v.visited == False:
                    discovered_lst.append([v, v.distance, v.previous])
                    v.discovered_vertex()

        return visited_lst

    def backtrack_path(self, visited_lst, destination):
        index = ord(destination) - 65
        reversed_path = []
        path = ""

        reversed_path.append(destination)
        while visited_lst[index][2] != None:

            reversed_path.append(visited_lst[index][2])
            index = ord(visited_lst[index][2]) - 65

        for i in range(len(reversed_path)-1, -1, -1):
            if i != 0:
                path = path + reversed_path[i] + " ---> "
            else:
                path = path + reversed_path[i]
        return path

    def dijikstra(self):
        pass


class Vertex:
    def __init__(self, id):
        # Each vertex store a list of edges from it.
        self.id = id
        self.edges = []
        self.visited = False
        self.discovered = False
        self.distance = 0
        self.previous = None

    def discovered_vertex(self):
        self.discovered = True

    def visited_vertex(self):
        self.visited = True


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


if __name__ == "__main__":
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    graph = Graph(lst)
    res = graph.bfs_shortest_path()
    print(graph.backtrack_path(res, 'H'))
    # print(res)
    # for item in res:
    #     print(item[0].id, item[1], item[2])
    # print(item)
    # graph.bfs(Vertex(1))

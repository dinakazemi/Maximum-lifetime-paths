"""
Vertex Class

Holds the dummy vertex module for the lifetime graph.
vertex in the graph.
Stores the id of the vertex and the edges.

Eg. if this is Vertex1 and it connects to Vertex2
this.edges[2] == edge between V1 and V2.
"""


class Vertex:
        """
        The vertex class, holds the 'id' of the vertex and the
        edges connected.
        To be inserted into the graph.
        """

        def __init__(self, id):
                """
                Initialises the vertex and the empty set of edges.
                :param id: The vertex ID
                """
                self._id = id
                self.edges = {}

        def get_id(self):
                """
                Get the vertex ID.
                :return: The id of the vertex
                """
                return self._id

        def get_edges(self):
                """
                Return the edges for this node.
                :return: The map of edges for this node
                """
                return self.edges

        def get_edge_to(self, vertex):
                """
                Return the edge from this vertex to the given vertex if exists.
                :param vertex: (Vertex class) The destination for the edge.
                :return: The edge to the vertex or None
                """
                try:
                        to_return = self.edges[vertex.get_id()]
                        return to_return
                except KeyError:
                        return None

        def add_edge(self, v, e):
                """
                Add the edge to the "Adjacency list".
                :param v: (Vertex) the vertex this edge is connected to.
                :param e: The edge between this vertex and the given vertex.
                """
                self.edges[v.get_id()] = e

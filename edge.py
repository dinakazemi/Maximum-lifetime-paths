"""
Edge class

Provides the "lifetime" between two vertices
that are in a graph.
"""


class Edge:
        """
        The edge class holds the lifetime between two vertices.
        """

        def __init__(self, vertex_a, vertex_b, lifetime):
                """
                Initialises the Edge
                :param vertex_a: The vertex to connect the edge to
                :param vertex_b: The vertex to connect the edge to
                :param lifetime: Lifetime between the two vertices
                """
                self.vertexA = vertex_a
                self.vertexB = vertex_b
                self.lifetime = lifetime

        def __repr__(self):
                """
                ***DO NOT CHANGE***
                Allows the edge to be printed in the results.
                :return: String representation of the edge.
                """
                return "V{}-{}-V{}".format(self.vertexA.get_id(), self.lifetime, self.vertexB.get_id())

        def get_lifetime(self):
                """
                Gets the lifetime of this edge.
                :return: The lifetime of the edge.
                """
                return self.lifetime

        def get_a(self):
                """
                Return the vertex A of the edge.
                :return: vertex A
                """
                return self.vertexA

        def get_b(self):
                """
                Return the vertex B of the edge.
                :return: vertex B
                """
                return self.vertexB
        def set_lifetime(self,l):
                self.lifetime = l

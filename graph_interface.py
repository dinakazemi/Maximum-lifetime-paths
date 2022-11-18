"""
Interface for the lifetime graph.

Provides the methods that are required to have the lifetime
graph.
"""

import abc


class GraphInterface(metaclass=abc.ABCMeta):
    """
    Graph Interface
    Implements the key methods required to find the max lifetime path.

    - add_edge(a, b)
    - edges()
    - max_lifetime_path(start, end)
    """

    @abc.abstractmethod
    def add_edge(self, a, b, lifetime):
        """
        Adds an edge with a lifetime between two vertices.
        :param a: Index/ID of Vertex A in the edge.
        :param b: Index/ID of Vertex B in the edge.
        :param lifetime: Lifetime between Vertex A and B
        """
        pass

    @abc.abstractmethod
    def edges(self):
        """
        Get the edges in the graph.
        :return list of edges.
        """
        pass

    def lifetime_path(self, start_vertex, end_vertex):
        """
        Get the "max lifetime path" between two vertices, return
        the path and the minimum lifetime in the path.
        :param start_vertex: (int/index of the vertex) The vertex to begin the path.
        :param end_vertex: (int/index of the vertex) The vertex to end the path.
        :return: The list of edges in the path.
        """
        pass

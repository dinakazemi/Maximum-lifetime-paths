"""
Lifetime Graph

Holds a graph of vertices where the edges between vertices has a lifetime.
The graph is implemented using an adjacency list.
"""

from graph_interface import GraphInterface
from vertex import Vertex
from edge import Edge
from priority_q import priority_q
class LifetimeGraph(GraphInterface):

        def __init__(self):
                """
                Initialises the graph with an empty adjacency list.
                """
                self.adjacency_list = {}

        def add_edge(self, a, b, lifetime):
                """
                Add an edge to the graph between the given vertices (a, b)

                If the vertex doesn't exist, then create the vertex and add it to
                the adjacency list.

                :param a: (int) - Vertex A ID
                :param b: (int) - Vertex B ID
                :param lifetime:  Lifetime of the edge.
                """
                v_a = Vertex(a)
                v_b = Vertex(b)
                e = Edge(v_a, v_b, lifetime)
                found_a = False
                found_b = False
                for v in self.adjacency_list.keys():
                        if v.get_id() == v_b.get_id():
                                found_b = True
                                v_b = v
                        if v.get_id() == v_a.get_id():
                                found_a = True
                                v_a = v
                if (found_a == False and found_b == False):
                        self.adjacency_list[v_a] = [v_b]
                        self.adjacency_list[v_b] = [v_a]
                        v_a.add_edge(v_b,e)
                        v_b.add_edge(v_a, e)
                        #print ("2")
                elif found_a == True and found_b == False:
                        self.adjacency_list[v_b] = [v_a]
                        self.adjacency_list[v_a].append(v_b)
                        v_a.add_edge(v_b,e)
                        v_b.add_edge(v_a, e)
                        #print ("3")
                elif found_a == False and found_b == True:
                        self.adjacency_list[v_a] = [v_b]
                        self.adjacency_list[v_b].append(v_a)
                        v_a.add_edge(v_b,e)
                        v_b.add_edge(v_a, e)
                else:
                        existing_e = v_a.get_edge_to(v_b)
                        if existing_e == None:
                                self.adjacency_list[v_a].append(v_b)
                                self.adjacency_list[v_b].append(v_a)
                                v_a.add_edge(v_b,e)
                                v_b.add_edge(v_a, e)
                        else:
                                existing_e.set_lifetime(lifetime)
                                #print ("5")
        def edges(self):
                """
                Return the set of edges in the graph

                The edges should be returned in order of vertices,
                e.g. loop through vertices from 0-N.

                :return: List of edges in the graph.
                """
                # TODO implement this
                sorted_list = self.sort_adjacancy_list()
                edges = []
                for v in sorted_list.keys():
                        edge_v = v.get_edges()
                        for e in edge_v.values():
                                if not e in edges:
                                        edges.append(e)
                return edges
                        

        def lifetime_path(self, start_vertex, end_vertex):
                """
                Return the maximum lifetime path between two vertices.

                :param start_vertex: (int) The ID of vertex A to begin the path.
                :param end_vertex: (int) The ID of vertex B to end the path.
                :return: The list of edges that create the path.
                """
                # TODO implement this
                v_a = None
                v_b = None
                for v in self.adjacency_list.keys():
                        if v.get_id() == start_vertex:
                                v_a = v
                        if v.get_id() == end_vertex:
                                v_b = v
                if (v_a == None or v_b == None):
                        return []
                #print (parent[v_a])
                # for i in parent.items():
                #         if (i[1] == None):
                #                 print (i[0].get_id() , None)
                #         else:
                #                 print (i[0].get_id() , i[1].get_id())
                parent = self.Dijkstra(v_a, v_b)
                result = []
                vertex = v_b
                while True:
                        p = parent[vertex]
                        if vertex == v_b:
                                result.append(vertex.get_edge_to(p))
                        else:
                                result.append(p.get_edge_to(vertex))
                        for i in parent.items():
                                if i[0] == p:
                                        vertex = i[0]
                                        break
                        if vertex == v_a:
                                break
                        
                return result[::-1]
        def Dijkstra (self,start, end):
                life_time = {}
                parent = {}
                for v in self.adjacency_list.keys():
                        if v.get_id() == start.get_id():
                                life_time[v] = 0
                        else:
                                life_time[v] = -1
                        parent[v] = None
                q = priority_q()
                for v in self.adjacency_list.keys():
                         q.put(v, life_time[v])
                while not q.is_empty():
                        u = q.remove_max()
                        str_u = str(u.get_id())
                        #print ("vertex with max id: "+ str_u)
                        for z in self.adjacency_list[u]:
                                if not z in q.get_keys():
                                        continue
                                str_z = str(z.get_id())
                                #print ("neighbour's id: " + str_z)
                                if u.get_edge_to(z).get_lifetime()> life_time[z]:
                                        life_time[z] = u.get_edge_to(z).get_lifetime()
                                        q.update(z, life_time[z])
                                        parent[z] = u
                                        #print (life_time[z], parent[z].get_id())
                return parent
        def sort_adjacancy_list(self):
                ids = self.get_ids()
                #print(ids)
                n = len(ids)
                for i in range(1, n):
                        x = ids[i]
                        j = i
                        while j > 0 and x < ids[j-1]:
                                ids[j] = ids[j-1]
                                j = j - 1
                        #print (ids)
                        ids[j] = x
                
                sorted_adjacancy_list = {}
                for id in ids:
                        for v in self.adjacency_list.keys():
                                if id == v.get_id():
                                        sorted_adjacancy_list[v] = self.adjacency_list[v]
                return sorted_adjacancy_list
                
        def get_ids(self):
                ids = []
                for v in (self.adjacency_list.keys()):
                        ids.append(v.get_id())
                #print (ids)
                return ids
def main():
        g = LifetimeGraph()
        g.add_edge(0,1,2)
        g.add_edge(0,2,1)
        g.add_edge(1,2,3)
        g.add_edge(2,3,4)
        g.add_edge(3,4,2)
        g.add_edge(3,5,5)
        g.add_edge(4,5,7)
        for e in g.edges():
                print (e)
        print (g.lifetime_path(1, 4))
if __name__ == "__main__":
        main()

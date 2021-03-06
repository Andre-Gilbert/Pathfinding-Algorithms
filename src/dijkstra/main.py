"""Runs Dijkstra's Algorithm.

Typical usage example:
    v_a = Vertex('A')
    v_b = Vertex('B')
    v_c = Vertex('C')
    v_d = Vertex('D')
    v_e = Vertex('E')
    v_f = Vertex('F')
    vertices = {v_a, v_b, v_c, v_d, v_e, v_f}

    e_a_b = Edge(v_a, v_b, 7)
    e_a_c = Edge(v_a, v_c, 9)
    e_a_f = Edge(v_a, v_f, 14)
    e_b_c = Edge(v_b, v_c, 10)
    e_b_d = Edge(v_b, v_d, 15)
    e_c_d = Edge(v_c, v_d, 11)
    e_c_f = Edge(v_c, v_f, 2)
    e_d_e = Edge(v_d, v_e, 6)
    e_f_e = Edge(v_f, v_e, 9)
    edges = {e_a_b, e_a_c, e_a_f, e_b_c, e_b_d, e_c_d, e_c_f, e_d_e, e_f_e}

    graph = Graph(vertices, edges)

    print("\nDijkstra Lazy Version:")
    print("-" * 31)
    dijkstra_lazy(graph, v_a, v_e)

    # Reset visited vertices
    for vertex in graph.vertices:
        vertex.visited = False

    print("\nDijkstra Eager Version:")
    print("-" * 31)
    dijkstra_eager(graph, v_a, v_e)
"""
from algorithms import dijkstra_eager, dijkstra_lazy
from data_structures import Edge, Graph, Vertex

if __name__ == '__main__':
    v_a = Vertex('A')
    v_b = Vertex('B')
    v_c = Vertex('C')
    v_d = Vertex('D')
    v_e = Vertex('E')
    v_f = Vertex('F')
    vertices = {v_a, v_b, v_c, v_d, v_e, v_f}

    e_a_b = Edge(v_a, v_b, 7)
    e_a_c = Edge(v_a, v_c, 9)
    e_a_f = Edge(v_a, v_f, 14)
    e_b_c = Edge(v_b, v_c, 10)
    e_b_d = Edge(v_b, v_d, 15)
    e_c_d = Edge(v_c, v_d, 11)
    e_c_f = Edge(v_c, v_f, 2)
    e_d_e = Edge(v_d, v_e, 6)
    e_f_e = Edge(v_f, v_e, 9)
    edges = {e_a_b, e_a_c, e_a_f, e_b_c, e_b_d, e_c_d, e_c_f, e_d_e, e_f_e}

    graph = Graph(vertices, edges)

    print("\nDijkstra Lazy Version:")
    print("-" * 31)
    dijkstra_lazy(graph, v_a, v_e)

    # Reset visited vertices
    for vertex in graph.vertices:
        vertex.visited = False

    print("\nDijkstra Eager Version:")
    print("-" * 31)
    dijkstra_eager(graph, v_a, v_e)

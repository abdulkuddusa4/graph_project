from functools import reduce
from graph import Graph,ramdom_graph_generator

graph = Graph({
    ('a','b'):2,
    ('a','d'):8,
    ('b','e'):6,
    ('b','d'):5,
    ('d','e'):3,
    ('d','f'):2,
    ('e','c'):5,
    ('f','e'):1,
    ('f','c'):3,
    ('d','h'):20,
    ('h','i'):10,
})
graph.show_shortest_path('a','h')

# graph = ramdom_graph_generator(['a','b','c','d','k','j','iu'])
# graph.show_shortest_path('a')
# print(graph.shortest_path('a','b'))

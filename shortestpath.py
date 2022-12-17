#import networkx as nx
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", city.from_dict)
city1 = nodes["aberdeen"]
city2 = nodes["perth"]

#for i in path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
#    print(f"{i}.", "→" .join(city.name for city in path))


from graph import shortest_path
"→".join(city.name for city in shortest_path(graph, city1, city2))

def by_latitude(city):
    return -city.latitude

"→".join(
    city.name 
    for city in shortest_path(graph, city1, city2, by_latitude))

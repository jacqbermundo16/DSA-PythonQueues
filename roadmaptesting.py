from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dicts)

nodes["london"]

print(graph)

for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)

for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)
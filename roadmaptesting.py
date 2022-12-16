from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dicts)

nodes["london"]

print(graph)
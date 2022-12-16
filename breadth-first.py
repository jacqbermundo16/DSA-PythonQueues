import networkx as nx
from graph import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in ns.bfs_tree(graph, nodes["eidenburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Fpound:", node.name, node.year)
        break

else:
    print("Nout Found")

def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key-by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["eidenburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")

    

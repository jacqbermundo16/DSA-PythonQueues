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
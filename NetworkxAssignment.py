from pylab import *
import networkx as nx

g = nx.Graph()

g.add_nodes_from(['Jason', 'Alex', 'Will', 'Tim', 'Khizar', 'Tyler', 'Micheal', 'Zel'])

g.add_edges_from([('Jason', 'Alex'), ('Jason', 'Will'), ('Jason', 'Tim'), ('Jason', 'Khizar'), ('Jason', 'Tyler'), ('Jason', 'Micheal'), ('Jason', 'Zel')])

g.add_edges_from([('Will', 'Alex'), ('Will', 'Khizar'), ('Will', 'Tyler'), ('Will', 'Micheal')])

g.add_edges_from([('Tyler', 'Khizar'), ('Tyler', 'Micheal')])

g.add_edges_from([('Khizar', 'Micheal')])


nx.draw(g, with_labels = True, edge_color = 'red')

show()
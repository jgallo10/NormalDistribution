from pylab import *
import networkx as nx

g = nx.Graph()
#position = nx.spring_layout(g)

g.add_nodes_from(['Jason', 'Zel', 'Mooney', 'Caitlyn', 'Josh', 'Alex', 'Jay', 'Abby', 'Gabby', 'CJ'])

g.add_nodes_from(['24', '28', '25', '23'])

g.add_nodes_from(['Teacher', 'Engineer', 'Employment', 'Nurse', 'Real-estate', 'Photographer'])

g.add_edges_from([('Jason', 'Engineer'), ('Alex', 'Engineer'), ('Jay', 'Engineer'), ('Gabby', 'Engineer')])

g.add_edges_from([('Zel', 'Employment'), ('Mooney', 'Employment'), ('Caitlyn', 'Nurse'), ('Abby', 'Teacher'), ('CJ', 'Real-estate'), ('Josh', 'Photographer')])

g.add_edges_from([('Jason', 'Zel'), ('Jason', 'Mooney'), ('Jason', 'Caitlyn'), ('Jason', 'Josh'), ('Jason', 'Alex'), ('Jason', 'Jay'), ('Jason', 'Abby'), ('Jason', 'Gabby'), ('Jason', 'CJ')])

g.add_edges_from([('Zel', 'Mooney'), ('Zel', 'Caitlyn'), ('Zel', 'Josh'), ('Zel', 'CJ')])

g.add_edges_from([('CJ', 'Mooney'), ('CJ', 'Josh'), ('CJ','Caitlyn')])

g.add_edges_from([('Mooney', 'Josh'), ('Mooney', 'Caitlyn')])

g.add_edges_from([('23', 'Abby')])

g.add_edges_from([('24', 'Jason'), ('24', 'Alex'), ('24', 'Gabby')])

g.add_edges_from([('25', 'Caitlyn'), ('25', 'Josh'), ('25', 'Jay'), ('25', 'CJ')])

g.add_edges_from([('28', 'Mooney'), ('28', 'Zel')])

nx.draw(g, with_labels = True)

show()
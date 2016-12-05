import networkx as nx

from pylab import *

g = nx.Graph()


global ncounter
ncounter = 1
g.add_node(ncounter, {'energy': 1.0, 'visited': False})

def add_nodes(g, emin, x):
    global ncounter
    for node in  g.nodes():
       if not g.node[node]['visited']:
            g.node[node]['visited'] = True
            e = g.node[node]['energy']
            if (e * (1 - 2 * x)) >= emin:
                ncounter += 1
                newnode = '*%s/%1.3g'%(ncounter, e * (1 - 2 * x))
                g.add_node(newnode, {'energy': e * (1 - 2 * x), 'visited':False})
                g.add_edge(node, newnode)
            if e * x >= emin:
                ncounter += 1
                newnode = '%s/%1.3g'%(ncounter, e * x)
                g.add_node(newnode, {'energy': e * x, 'visited': False})
                g.add_edge(node, newnode)
            if e * x >= emin:
                ncounter += 1
                newnode = '%s/%1.3g'%(ncounter, e * x)
                g.add_node(newnode, {'energy': e * x, 'visited': False})
                g.add_edge(node, newnode)

    else:
        return True
    return False



for k in range(1000):
    add_nodes(g, 0.01, 0.3)

print(g.nodes())

#nx.draw_networkx(g)

from networkx.drawing.nx_agraph import write_dot

write_dot(g,'test.dot')

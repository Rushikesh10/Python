# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:15:24 2019

@author: Rushikesh
"""

import networkx as nx
import matplotlib.pyplot as py
G=nx.Graph()
#l=[1,2,3]
#G.add_nodes_from(l)
#G.add_node(1)
#G.add_node(2)
#G.add_node(3)
#G.add_edge(1,2)
#G.add_edge(2,3)
#G.add_edge(1,3)
#G=nx.complete_graph(10)
G=nx.gnp_random_graph(10,0.2)
print(G.nodes())
print(G.edges())

nx.draw(G)
py.show()
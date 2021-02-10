from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from Tree_without_node import Tree

graphviz = GraphvizOutput(output_file='filter_none.png')

with PyCallGraph(output=graphviz):
    tree = Tree()
    for i in range(1,100):
        tree.insert(i)
#################################################################################
########################## Fichier d'exemple et d'aide ##########################
#################################################################################

import pandas as pd
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt
import netgraph
from bokeh.io import output_file, show
from bokeh.models import (PanTool, SaveTool, BoxZoomTool, WheelZoomTool, Circle, HoverTool, MultiLine, Plot, Range1d, ResetTool,)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx, figure
os.chdir('D:/Travail/Master 1/Projet intégré/DATAVIZ_2')

author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)

plt.ion() # "Turn the interactive mode on."

G=nx.Graph()
# adding just one node:
G.add_node("a")
# a list of nodes:
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)
# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

nx.draw(G)
plt.show() # display

cities = {0:"Toronto",1:"London",2:"Berlin",3:"New York"}
H=nx.relabel_nodes(G,cities)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())


def addNodes(G, *nodes):
    for arg in nodes:
        G.add_node(arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display


G=nx.Graph()
addNodes(G, "Noeud1", "Noeud2", "Noeud3")

# Ex. afficherPublicationAuteur(G, "nom auteur", *publications)
# *publications étant toutes les publications de l'auteur qu'on veut afficher
# Il faudra alors relier l'auteur à toutes les publications (1 unique auteur pour l'instant)

def afficherPublicationsAuteur(G, auteur, *publications):
    G.add_node(auteur)
    
    for arg in publications:
        G.add_node(arg)
        G.add_edge(auteur,arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display


G=nx.Graph()    
afficherPublicationsAuteur(G, "Auteur1", "publi1", "publi2", "publi3")

################################
###### Test de différence entre *args et **kwargs
#Si un argument de position suit *args , ce sont des arguments de mots-clés uniquement 
#pouvant être transmis uniquement par nom.
# Exemple :
def func(a, b, *args, x, y):
    print(a, b, args, x, y)

func(1, 2, 3, 4, x=5, y=6)

# *args pour un nombre variable d'arguments
def display(*argv):  
    for arg in argv:  
        print (arg) 
    
display('Hello', 'Welcome', 'to', 'WayToLearnX')

# Résultat :
# Hello
# Welcome
# to
# WayToLearnX

###

def display(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
display(id=1, name='Alex', age=23)

# Résultat :
# id == 1
# name == Alex
# age == 23

# Autre exemple
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

# Résultat :
# Data type of argument: <class 'dict'>
# Firstname is Sita
# Lastname is Sharma
# Age is 22
# Phone is 1234567890

# Data type of argument: <class 'dict'>
# Firstname is John
# Lastname is Wood
# Email is johnwood@nomail.com
# Country is Wakanda
# Age is 25
# Phone is 9876543210

#####################################################

# Prepare Data
G = nx.karate_club_graph()

SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "black", "red"
edge_attrs = {}

for start_node, end_node, _ in G.edges(data=True):
    edge_color = SAME_CLUB_COLOR if G.nodes[start_node]["club"] == G.nodes[end_node]["club"] else DIFFERENT_CLUB_COLOR
    edge_attrs[(start_node, end_node)] = edge_color

nx.set_edge_attributes(G, edge_attrs, "edge_color")

# Show with Bokeh
plot = Plot(plot_width=400, plot_height=400,
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot.title.text = "Graph Interaction Demonstration"

node_hover_tool = HoverTool(tooltips=[("Test", "@index"), ("club", "@club"), ("Test2", "@test2")])
plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color", line_alpha=0.8, line_width=1)
plot.renderers.append(graph_renderer)
output_file("interactive_graphs.html")
show(plot)



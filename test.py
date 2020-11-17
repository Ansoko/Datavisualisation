import pandas as pd
import numpy as np

author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)

keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/keyword.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_keywords = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_keywords.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/venue.csv", engine='python', encoding= 'unicode_escape', error_bad_lines=False)
year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/year.csv", engine='python', encoding= 'unicode_escape', error_bad_lines=False)

import os
os.chdir('D:/Travail/Master 1/Projet intégré/DATAVIZ_2')

import networkx as nx
import matplotlib.pyplot as plt
plt.ion() # "Turn the interactive mode on."
import netgraph

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

################################

# Faire le zoom sur un seul "auteur principal"
# Faire des noeuds "co-auteur" reliés à cet "auteur principal" (via une boucle for ?)
# Chaque noeud "publication" qui part de "co-auteur" est donc indirectement relié à "auteur principale"
# Dans le label du noeud, il faudra préciser si co-écrit ? 
#(donc dans la boucle qui relie "co-auteur" et "publication")
# Comme ça, on pourra distinguer si les noeuds reliés à auteur principal sont des co-auteurs ou des publications
# Peut-être même nommer les arguments à l'appel de la fonction (G = G, auteur = "auteur1", publications....)
# Les noeuds des co-auteur seront d'une autre couleur que celui des articles et de l'auteur principal
author = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/author.csv", 
                    engine='python', error_bad_lines=False)
print(author.head(10))
print(author.info())

publication = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/publication.csv", 
                          engine='python', error_bad_lines=False)
print(publication.head(10))
print(publication.info())

publication_author = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/publication_author.csv", 
                                 engine='python', error_bad_lines=False)
print(publication_author.head(10))
print(publication_author.info())


# On récupère l'id de l'auteur envoyé en argument (via le champ de texte de l'interface par exemple)
def get_id_author(name):
    a = list(author.id_author[author.name_author == name])
    return a[0]

# Puis on essaye de trouver les id de publications affiliés à l'auteur précédent
# On veut donc entrer un id d'auteur et sortir une liste des id de toutes ses publications
def get_id_publication(idAuthor):
    return list(publication_author.id_publication[publication_author.id_author == idAuthor])

# On récupère le nom de tous les articles à partir des id de publication d'un auteur
def get_name_publication(list_Publication):
    ls = list()
    for i in list_Publication :
        a = list(publication.article_title[publication.id_publication == i])
        ls.append(a[0])
    return ls

def get_date_publication(list_Publication):
    ls = list()
    for i in list_Publication :
        a = list(publication.date_pub[publication.id_publication == i])
        ls.append(a[0])
    return ls

#idAuthor = get_id_author("A Min Tjoa") # 1 publication
idAuthor = get_id_author("A Min Tjoa") # A Min Tjoa       id_t/AMinTjoa
print("idAuthor : " + str(idAuthor))

listPublications = get_id_publication(idAuthor)

listPublications = get_id_publication("id_56/11306")
listPublications = get_id_publication("id_43/3031")

print("listPublications : " + str(listPublications))

listNamePublications = get_name_publication(listPublications)
print("listNamePublications : " + str(listNamePublications))


# Permet de récupérer la liste des titre d'article d'un auteur
authorName = "A Min Tjoa"
listNamePublications = get_name_publication(get_id_publication(get_id_author(authorName)))
listDatePublications = get_date_publication(get_id_publication(get_id_author(authorName)))
print("listNamePublications : " + str(listNamePublications))


def addNodes(G, *nodes):
    for arg in nodes:
        G.add_node(arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display

# Ex. afficherPublicationAuteur(G, "nom auteur", *publications)
# *publications étant toutes les publications de l'auteur qu'on veut afficher
# Il faudra alors relier l'auteur à toutes les publications (1 unique auteur pour l'instant)
# def afficherPublicationsAuteur(G, auteur, *publications):
#     G.add_node(auteur)
    
#     for arg in publications:
#         G.add_node(arg)
#         G.add_edge(auteur,arg)
        
#     nx.draw(G, with_labels=True)
#     plt.show() # display


# G = nx.Graph()    
#afficherPublicationsAuteur(G, authorName, "publi1", "publi2", "publi3")

def afficherPublicationsAuteur(G, auteur, publications):
    G.add_node(auteur)
    
    for arg in publications:
        G.add_node(arg)
        G.add_edge(auteur,arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display

G = nx.Graph()       
afficherPublicationsAuteur(G, authorName, listNamePublications) # Afficher le titre des publications

G = nx.Graph()       
afficherPublicationsAuteur(G, authorName, listDatePublications) # Afficher la date des publications

# Afficher le nom du nom avec le mouse over
import networkx as nx
from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool, MultiLine, Plot, Range1d, ResetTool,)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx

plot = Plot(plot_width=400, plot_height=400, x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot.title.text = "Graphe intéractif"
node_hover_tool = HoverTool(tooltips=[("Test", "@index"), ("club", "@club"), ("Test2", "@test2")])
plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())
graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
plot.renderers.append(graph_renderer)
output_file("interactive_graphs.html")
show(plot)
# Pouvoir afficher les titres d'articles que sui on passe le curseur sur le noeud de l'article


def test(G, auteur, publications):
    G.add_node(auteur)
    
    for arg in publications:
        G.add_node(arg)
        G.add_edge(auteur,arg)
        
    #nx.draw(G, with_labels=True)
    netgraph.draw(graph)
    plot_instance = netgraph.InteractiveGraph(graph)
    plt.show() # display


graph = nx.Graph()       
test(graph, authorName, listDatePublications)


import networkx as nx

from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx

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


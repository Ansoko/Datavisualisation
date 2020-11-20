###########################################################################
####################### Fichier du code fonctionnel #######################
###########################################################################

######################################################### Début #########################################################
######## Importation des librairies ########
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
########################################################## Fin ##########################################################


''' Objectifs :
Faire le zoom sur un seul "auteur principal"
Faire des noeuds "co-auteur" reliés à cet "auteur principal" (via une boucle for ?)
Chaque noeud "publication" qui part de "co-auteur" est donc indirectement relié à "auteur principale"
Dans le label du noeud, il faudra préciser si co-écrit ? 
(donc dans la boucle qui relie "co-auteur" et "publication")
Comme ça, on pourra distinguer si les noeuds reliés à auteur principal sont des co-auteurs ou des publications
Peut-être même nommer les arguments à l'appel de la fonction (G = G, auteur = "auteur1", publications....)
Les noeuds des co-auteur seront d'une autre couleur que celui des articles et de l'auteur principal
'''


######################################################### Début #########################################################
######## Importation des données ########
author = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/author.csv", engine='python', error_bad_lines=False)
print(author.head(10))
print(author.info())

publication = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/publication.csv", engine='python', error_bad_lines=False)
print(publication.head(10))
print(publication.info())

publication_author = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/publication_author.csv", engine='python', error_bad_lines=False)
print(publication_author.head(10))
print(publication_author.info())
########################################################## Fin ##########################################################


######################################################### Début #########################################################
''' On récupère l'id de l'auteur envoyé en argument (via le champ de texte de l'interface par exemple)
INPUT :
    - name (string) : nom de l'auteur
OUPUT :
    - a[0] (string) : renvoie l'id de l'auteur en format string '''
def get_id_author(name):
    a = list(author.id_author[author.name_author == name])
    return a[0]
########################################################## Fin ##########################################################


######################################################### Début #########################################################
''' On trouve les id de publications affiliés à un auteur
    On veut donc entrer un id d'auteur et sortir une liste des id de toutes ses publications
INPUT :
    - idAuthor (string) : id de l'auteur
OUTPUT :
    - (list) : renvoie l'id des publications de l'auteur '''
def get_id_publication(idAuthor):
    return list(publication_author.id_publication[publication_author.id_author == idAuthor])
########################################################## Fin ##########################################################


######################################################### Début #########################################################
''' On récupère le nom de tous les articles à partir des id de publications d'un auteur
INPUT : 
    - list_publication (list) : liste des id des publications d'un auteur
OUTPUT :
    - ls (list) : renvoie la liste des noms de chaque publication d'un auteur '''
def get_name_publication(list_publication):
    ls = list()
    for i in list_publication :
        a = list(publication.article_title[publication.id_publication == i])
        ls.append(a[0])
    return ls
########################################################## Fin ##########################################################


######################################################### Début #########################################################
''' On récupère la date des publications à partir des id de publications d'un auteur
INPUT :
    - list_publication (list) : liste des id des publications d'un auteur
OUPUT : 
    - ls (list) : renvoie la liste des dates de chaque publication d'un auteur '''
def get_date_publication(list_publication):
    ls = list()
    for i in list_publication :
        a = list(publication.date_pub[publication.id_publication == i])
        ls.append(a[0])
    return ls
########################################################## Fin ##########################################################


######################################################### Début #########################################################
####### Tester les fonctions get ci-dessus #######
# idAuthor = get_id_author("A Min Tjoa") # A Min Tjoa, ayant pour id 'id_t/AMinTjoa'
# print("idAuthor : " + str(idAuthor))

# listPublications = get_id_publication(idAuthor)
# listPublications = get_id_publication("id_56/11306")
# listPublications = get_id_publication("id_43/3031")
# print("listPublications : " + str(listPublications))

# listNamePublications = get_name_publication(listPublications)
# print("listNamePublications : " + str(listNamePublications))
########################################################## Fin ##########################################################


######################################################### Début #########################################################
''' Ajoute un noeud au graphe pour chaque publication d'un auteur
INPUT : 
    - G (graph) : graphe (vide ou pas) auquel on va ajouter des noeuds
    - *nodes (string) : nombre indéfini d'un élément de publication (titre, date, etc.) qu'on ajoute au graphe
OUTPUT :
    - Aucun : cela va seulement ajouter les noeuds au graphe '''
def addNodes(G, *nodes):
    for arg in nodes:
        G.add_node(arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display
########################################################## Fin ##########################################################


######################################################### Début #########################################################
''' Relie l'auteur à toutes ses publications (1 unique auteur pour l'instant)
INPUT : 
    - G (graph) : graphe (vide ou pas) auquel on va ajouter des noeuds
    - auteur (string) : nom de l'auteur
    - publications (list) : liste des publications de l'auteur
OUTPUT :
    - Aucun : cela va seulement générer le graphe '''
def afficherPublicationsAuteur(G, auteur, publications): # *publication si on reçoit paramètre par paramètre
    G.add_node(auteur)
    
    for arg in publications:
        G.add_node(arg)
        G.add_edge(auteur,arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display
########################################################## Fin ##########################################################


# Permet de récupérer la liste des titres / dates de publications du nom d'un auteur
authorName = "A Min Tjoa"
listNamePublications = get_name_publication(get_id_publication(get_id_author(authorName))) # Titres
listDatePublications = get_date_publication(get_id_publication(get_id_author(authorName))) # Dates
print("listNamePublications : " + str(listNamePublications))

G = nx.Graph()       
afficherPublicationsAuteur(G, authorName, listNamePublications) # Afficher le titre des publications

G = nx.Graph()       
afficherPublicationsAuteur(G, authorName, listDatePublications) # Afficher la date des publications


# Afficher le nom du nom avec le mouse over et l'ouvrir sur un navigateur Web
plot = Plot(plot_width=400, plot_height=400, x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot.title.text = "Graphe intéractif"
node_hover_tool = HoverTool(tooltips=[("Titre", "@index"), ("Date", "@date")]) # exemple : (tooltips=[("Test", "@index"), ("club", "@club"), ("Test2", "@test2")])
plot.add_tools(node_hover_tool, PanTool(), WheelZoomTool(), BoxZoomTool(), ResetTool(), SaveTool()) # RangeTool, EditTool, Drag, Gesture, PointDrawTool
graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
plot.renderers.append(graph_renderer)
output_file("interactive_graphs.html")
show(plot)
# Peut-être qu'avec un dictionnaire de données plutôt qu'une liste en paramètre,
# on pourra extraire les clés Titre et Date ainsi que leurs valeurs respectives @titre et @date 
# $index pour l'indice du noeud, à ne pas confondre avec @index
# @QuelqueChose signifie que QuelqueChose est le nom d'une colonne du data source (donc la clé d'une clé-valeur ?)







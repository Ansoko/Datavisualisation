# Code permettant de créer un graphe avec un auteur dans le noeud principale et ses publications dans les noeuds secondaires
import pandas as pd
import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt
import netgraph
from bokeh.io import output_file, show
from bokeh.models import (PanTool, SaveTool, BoxZoomTool, WheelZoomTool, Circle, HoverTool, MultiLine, Plot, Range1d, ResetTool, ColumnDataSource)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx, figure
from bokeh.models.graphs import NodesAndLinkedEdges, EdgesAndLinkedNodes
os.chdir('D:/Travail/Master 1/Projet intégré/DATAVIZ_2')

author = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/author.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/publication.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("D:/Travail/Master 1/Projet intégré/DATAVIZ_2/publication_author.csv", engine='python', error_bad_lines=False)

# Récupération de l'id d'un auteur
def get_id_author(name):
    a = list(author.id_author[author.name_author == name])
    return a[0] # return a[0] pour juste avoir le nom de l'auteur

# Génération d'une liste de n fois le nom de l'auteur, pour qu'il soit affiché sur chaque noeud du graphe
def get_name_author(name, n):
    ls = list()
    for i in range(n):
        a = list(author.name_author[author.name_author == name])
        ls.append(a[0])
    return ls

# Récupération du nombre de publication d'un auteur pour l'afficher sur le noeud principale (celui de l'auteur)
def get_nb_publication_author(name):
    return list(author.nbr_publication[author.name_author == name])[0]

# Récupération des id des publications d'un auteur à partir de l'id d'un auteur
def get_id_publication(idAuthor):
    return list(publication_author.id_publication[publication_author.id_author == idAuthor])

# Récupération des noms des publications d'un auteur à partir de la liste des id de publication de l'auteur
def get_name_publication(list_publication):
    ls = list()
    for i in list_publication :
        a = list(publication.article_title[publication.id_publication == i])
        ls.append(a[0])
    return ls

# Récupération des dates des publications d'un auteur à partir de la liste des id de publication de l'auteur
def get_date_publication(list_publication):
    ls = list()
    for i in list_publication :
        a = list(publication.date_pub[publication.id_publication == i])
        ls.append(a[0])
    return ls

# Récupération des noms des catégories d'un auteur à partir de la liste des id de publication de l'auteur
def get_categ_publication(list_publication):
    ls = list()
    for i in list_publication :
        a = list(publication.categorie[publication.id_publication == i])
        ls.append(a[0])
    return ls

# Transformation de tous les éléments d'une liste par un id numérique (1, 2, 3, ..., n)
def get_transform_id(n):
    newList = list()
    for i in range(n):
        newList.append(str(i+1))
    return newList

# Création du graphe en commençant par le noeud principale (auteur) puis avec les noeuds secondaires (ses publications)
def afficherPublicationsAuteur(G, nomAuteur, publications):
    # Création du noeud principale
    G.add_node(nomAuteur) 
    
    # Création des noeuds secondaires
    fin = len(publications)-1
    for arg in publications:
        G.add_node(arg)
        if(arg != publications[fin]): # Permet d'éviter d'avoir une arête sans noeud 
            G.add_edge(nomAuteur,arg)
        
    nx.draw(G, with_labels=True)
    plt.show() # display


authorName = "A Min Tjoa"

# Listes des données des fichiers CSV à partir du nom d'un auteur
listIdPublications = get_id_publication(get_id_author(authorName)) # Id publications
listNamePublications = get_name_publication(get_id_publication(get_id_author(authorName))) # Titres
listDatePublications = get_date_publication(get_id_publication(get_id_author(authorName))) # Dates
listCategPublications = get_categ_publication(get_id_publication(get_id_author(authorName))) # Catégories

# A utiliser si on veut afficher des id simples (numériques) pour les publications
listIdPublications = get_transform_id(len(listIdPublications))

# Insertion des données concernant l'auteur au début des listes (noeud central, qui correspond à l'auteur) 
# pour pouvoir afficher toutes les données de l'auteur correctement
listIdPublications.insert(0, "Nombre : " + str(get_nb_publication_author(authorName)))
listNamePublications.insert(0, '---')
listDatePublications.insert(0, '---')
listCategPublications.insert(0, '---')

listNameAuthor = get_name_author(authorName, len(listIdPublications)) # Liste content les noms de l'auteur

# Création du graphe
G = nx.Graph()       
afficherPublicationsAuteur(G, authorName, listIdPublications) # On prend les id des publications pour créer chaque noeud secondaire
plot = Plot(plot_width=400, plot_height=400, x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
plot.title.text = "Graphe intéractif"

# Affichage des différents élément au survol d'un noeud
node_hover_tool = HoverTool(tooltips=[("Auteur", "@Nom_auteur"), ("Publication", "@publication"), ("Titre", "@Titre"), ("Date", "@Date"), ("Catégorie", "@Categ")])
# Outils qui apparaissent à côté du graphe pour se déplacer dessus, le sauvegarder, etc.
plot.add_tools(node_hover_tool, PanTool(), WheelZoomTool(), BoxZoomTool(), ResetTool(), SaveTool())

# Mise en place des données dans les différents noeuds
graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
graph_renderer.node_renderer.data_source.add(listNameAuthor, 'Nom_auteur')
graph_renderer.node_renderer.data_source.add(listIdPublications, 'publication')
graph_renderer.node_renderer.data_source.add(listNamePublications, 'Titre')
graph_renderer.node_renderer.data_source.add(listDatePublications, 'Date')
graph_renderer.node_renderer.data_source.add(listCategPublications, 'Categ')

# Affichage graphique des noeuds et des arêtes
graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
graph_renderer.node_renderer.hover_glyph = Circle(size=21, fill_color='red')
graph_renderer.edge_renderer.glyph = MultiLine(line_color='black', line_width=1)
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color='green', line_width=5)
graph_renderer.selection_policy = EdgesAndLinkedNodes()
graph_renderer.inspection_policy = NodesAndLinkedEdges()
plot.renderers.append(graph_renderer)

# On affiche le graphe dans une page HTML
output_file("interactive_graphs.html")
show(plot)

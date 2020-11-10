import pandas as pd

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
# Faire des noeuds "co-auteur" reliés à cette "auteur principal" (via une boucle for ?)
# Chaque noeud "publication" qui part de "co-auteur" est donc indirectement relié à "auteur principale"
# Dans le label du noeud, il faudra préciser si co-écrit ? 
#(donc dans la boucle qui relie "co-auteur" et "publication")
# Comme ça, on pourra distinguer si les noeuds reliés à auteur principal sont des co-auteurs ou des publications
# Peut-être même nommer les arguments à l'appel de la fonction (G = G, auteur = "auteur1", publications....)







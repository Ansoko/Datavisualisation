import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/keyword.csv", engine='python', error_bad_lines=False)
author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/author.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_author.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication.csv", engine='python', error_bad_lines=False)
year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/year.csv", engine='python', error_bad_lines=False)
venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/venue.csv", engine='python', error_bad_lines=False)
publication_year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_year.csv",engine='python',error_bad_lines=False)
publication_venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_venue.csv",engine='python',error_bad_lines=False)
publication_keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_keywords.csv",engine='python',error_bad_lines=False)
    
authorhead = author.head(300)
keyword_head = keyword.head(300)
publication_head = publication.head(300)
publication_author_head = publication_author.head(300)
year_head = year.head(300)
venue_head = venue.head(300)
publication_keyword_head = publication_keyword.head(300)
publication_year_head = publication_year.head(300)
publication_venue_head = publication_venue.head(300)

csv_counter_row = 1

#Liste des Graphes à partir des données CSV

GraphYear = nx.from_pandas_edgelist(year,'id_year','year')

GraphAuthor = nx.from_pandas_edgelist(authorhead, 'name_author', 'nbr_publication',create_using=nx.DiGraph)

GraphPublication = nx.from_pandas_edgelist(publication_head, 'id_publication', 'date_pub','article_title',create_using=nx.DiGraph)

GraphKeyword = nx.from_pandas_edgelist(keyword_head, 'keyword', 'nbr_used',create_using=nx.DiGraph)

Graph_Publication_Author = nx.from_pandas_edgelist(keyword_head, 'id_publication','keyword','nbr_use_keyword',create_using=nx.DiGraph)

# Tableau vide d'une liste de couleurs pour les noeuds des graphes.
# colors = []

# Création d'un Graphe vide

G = nx.Graph()
    
    
def afficher_graph_publications_datespubs():
    pos_publication = nx.random_layout(GraphPublication)
    colors = []
    labels = {}
    for node in GraphPublication:
        if node in publication_head["id_publication"].values:            
            colors.append("red") 
        if node in publication_head["date_pub"].values: 
            colors.append("yellow")
        if node in publication_head["article_title"].values:
            colors.append("blue")
        
    plt.figure(figsize=(20,20))    
    nx.draw(GraphPublication, pos_publication, node_size=1200, node_color=colors,linewidths=0.25,font_size=10, font_weight='bold', with_labels=True)
    plt.show()
    
afficher_graph_publications_datespubs()

def afficher_graph_acteurs_publications():
    pos_author = nx.random_layout(GraphAuthor)
    colors = []
    for node in GraphAuthor:
        if node in authorhead["name_author"].values:
            colors.append("green")
        if node in authorhead["nbr_publication"].values: 
            colors.append("blue")
    plt.figure(figsize=(20,20))   
    nx.draw(GraphAuthor, pos_author, node_size=1000, node_color=colors,linewidths=0.15,font_size=10, font_weight='bold', with_labels=True)
    plt.show()
    fig = go.Figure(data=go.Scatter(x=authorhead["name_author"].values, y=authorhead["nbr_publication"].values, mode='markers'))
    fig.show()
 
afficher_graph_acteurs_publications()

def afficher_graph_keyword_nbr_used():
    pos_keyword = nx.random_layout(GraphKeyword)
    colors = []
    for node in GraphKeyword:
        if node in keyword_head["keyword"].values:
            colors.append("red") 
        if node in keyword_head["nbr_used"].values: 
            colors.append("blue")
        
    plt.figure(figsize=(20,20))    
    
    nx.draw(GraphKeyword, pos_keyword, node_size=1200, node_color=colors,linewidths=0.25,font_size=10, font_weight='bold', with_labels=True)
    plt.show()

def afficher_graph_keyword():
    pos_publication_author = nx.random_layout(GraphKeyword)
    colors = []
    for node in Graph_Publication_Author:
        if node in publication_author_head["keyword"].values:
            colors.append("red") 
        if node in publication_author_head["nbr_use_keyword"].values: 
            colors.append("yellow")
    plt.figure(figsize=(20,20))  
    
    nx.draw(Graph_Publication_Author, pos_publication_author, node_size=1200, node_color=colors,linewidths=0.25,font_size=10, font_weight='bold', with_labels=True)
    plt.show()
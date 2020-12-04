# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:09:03 2020

@author: Nico
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go
import numpy as np
from requete import request

keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/keyword.csv", engine='python', error_bad_lines=False)
author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/author.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_author.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication.csv", engine='python', error_bad_lines=False)
year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/year.csv", engine='python', error_bad_lines=False)
venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/venue.csv", engine='python', error_bad_lines=False)
publication_year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_year.csv",engine='python',error_bad_lines=False)
publication_venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_venue.csv",engine='python',error_bad_lines=False)
publication_keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_keywords.csv",engine='python',error_bad_lines=False)
    

def add_edge(x, y, width):
    edge =  go.Scatter(x         = x,
                       y         = y,
                       line      = dict(width = width,
                                   color = 'blue'),
                       hoverinfo = 'text',
                       mode      = 'lines')
    return edge

def afficher_Graph(nom_auteur,dataset):
    cols = list()
    cols = dataset.columns.tolist()
    center_node = nom_auteur
    
    nbr_nodes = len(dataset)
    
    nodes_title = [nbr for nbr in range(nbr_nodes)]
    
    node_w = 10

    Graph = nx.Graph()
    Graph.add_node(center_node, size = 20) 

    for i in range(len(nodes_title)):
        Graph.add_node(nodes_title[i], size = node_w)
        Graph.add_edge(center_node, nodes_title[i], width = node_w)
    
    pos = nx.spring_layout(Graph)

    edge_trace = []
    
    for edge in Graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        current_trace = add_edge(
								[x0, x1, None],
								[y0, y1, None],
								width = 5
								)

        edge_trace.append(current_trace)


    node_trace = go.Scatter(x			= [],
                        	y				= [],
                        	text      		= [],
                        	textposition	= "top center",
                        	textfont_size	=   20,
                        	hoverinfo		= 'text',
							mode			= 'markers',
							marker		= dict(color	= [],
                                         		size		= [] ,
                                         		line=dict(
                color='black',
                width=1
            )))
    
    annotations = []
    
    info = len(dataset)-1
    
    i=-1
    for node in Graph.nodes():
        i=+1
        try:
            text = str(dataset.iloc[i,:].values)
        except:
            text="txt"
        hover_text = ""
		
        if(node == center_node):
            hover_text = tuple(["{0}".format(center_node)])
            color = tuple(['yellow'])
            size = tuple([2 * Graph.nodes[node]['size']])
        else:
            hover_text = tuple([text])
            color = tuple(['blue'])
            size = tuple([2 * Graph.nodes[node]['size']])
		
        x, y = pos[node]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['marker']['color'] += color
        node_trace['marker']['size'] += size
        node_trace['text'] += tuple([hover_text])
        annotations.append(
 		  dict(x=x,
               	 y=y,
                 	 text="<b> " + str(node) + "</b>",
                 	 xanchor='left',
                     titleside='right',
                	 xshift=10,
                 	 font=dict(color='black', size=10),
                 	 showarrow=False)
           )

        layout = go.Layout(
     	paper_bgcolor='rgba(0,0,0,0)',
     	plot_bgcolor='rgba(0,0,0,0)', 
     	xaxis =  {'showgrid': False, 'zeroline': False},
     	yaxis = {'showgrid': False, 'zeroline': False}, 
	)
    info = info - 1
    
    
    # creation de la figure du layout 
    fig = go.Figure(layout = layout)
    fig.update_layout(
    hoverlabel=dict(
        font_size=10,
        font_family="Rockwell"
    )
)
    
    for trace in edge_trace:
        fig.add_trace(trace)
    fig.add_trace(node_trace)
    fig.update_layout(showlegend = False)

    fig.update_xaxes(showticklabels = False)
    fig.update_yaxes(showticklabels = False)
    plot(fig)
    fig.show()

res = pd.DataFrame(request(["A. Antony Franklin", "2018"], ["author", "year"], ["date_pub"], {"publication"}))
afficher_Graph('"Johann" Sebastian Rudolph',res)


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy
"""
keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/keyword.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_author.csv", engine='python', error_bad_lines=False)
publication_keywords = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_keywords.csv", engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_venue.csv", engine='python', error_bad_lines=False)
publication_year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_year.csv", engine='python', error_bad_lines=False)
venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/venue.csv", engine='python' ,error_bad_lines=False)
"""
year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/year.csv", engine='python', error_bad_lines=False)
author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/author.csv", engine='python', error_bad_lines=False)

csv_counter_row = 1

GraphYear = nx.from_pandas_edgelist(year,'id_year','year')
oui = GraphYear.head()

GraphAuthor = nx.from_pandas_edgelist(author,'id_author','name_author','nbr_publication')

GraphYear.edges(data=True)
edge_labels = dict((year) for u, v, d in GraphYear.edges(data=True))
pos = nx.random_layout(GraphYear)
nx.draw(GraphYear, pos)
nx.draw_networkx_edge_labels(GraphYear, pos, edge_labels=edge_labels)
plt.show()
        
nx.draw(GraphYear)
nx.draw(GraphAuthor)


"""
G = nx.random_geometric_graph(200, 0.125)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, "pos")

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center
p = dict(nx.single_source_shortest_path_length(G, ncenter))

plt.figure(figsize=(8, 8))
nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=list(p.keys()),
    node_size=80,
    node_color=list(p.values()),
    cmap=plt.cm.Reds_r,
)

plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.axis("off")
plt.show()

"""
"""
for row in year:
        G.add_nodes_from(row, color = 'blue')

color_map = []

for n in G.nodes():
    if n == '':
        G.remove_node(n)
    color_map.append(G.node[n]['color'])
nx.draw_networkx(G, node_color = color_map, with_labels = True, node_size = 500)
"""
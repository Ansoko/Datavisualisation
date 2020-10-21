import pandas as pd

author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/author.csv", engine='python', error_bad_lines=False)

keyword = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/keyword.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_author.csv", engine='python', error_bad_lines=False)
publication_keywords = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_keywords.csv", engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_venue.csv", engine='python', error_bad_lines=False)
publication_year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/publication_year.csv", engine='python', error_bad_lines=False)
venue = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/venue.csv", engine='python' ,error_bad_lines=False)
year = pd.read_csv("D:/MasterInfo/Projet_Integre/GestionProjet/Gestion_de_projets/dataset/year.csv", engine='python', error_bad_lines=False)


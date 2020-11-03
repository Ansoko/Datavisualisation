import pandas as pd

author = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/author.csv", engine='python', error_bad_lines=False)
keyword = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/keyword.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_author.csv", engine='python', error_bad_lines=False)
publication_keywords = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_keywords.csv", engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_venue.csv", engine='python', error_bad_lines=False)
publication_year = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_year.csv", engine='python', error_bad_lines=False)
venue = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/venue.csv", engine='python', error_bad_lines=False)
year = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/year.csv", engine='python', error_bad_lines=False)

print(author.loc[author.name_author=='A. Andersson',])

#authordf = pd.DataFrame({'id_author':author.id_author,'name_author':author.name_author, 'nbr_publication':author.nbr_publication})


#df = pd.merge(pd.merge(author, publication_author, on='id_author'),pd.merge(publication,publication_keywords, on='id_publication'),on='id_publication')
#impossible car memory error

#authordf = pd.DataFrame({'id_author':author.id_author,'name_author':author.name_author, 'nbr_publication':author.nbr_publication})

#df = pd.merge(pd.merge(author, publication_author, on='id_author'),pd.merge(publication,publication_keywords, on='id_publication'),on='id_publication')
#impossible car memory error

print("*Liste de toutes les publications d'un auteur*")
nameAuthor = input("Entrez le nom d'un auteur : ")
authorOnTable = author.loc[author.name_author==nameAuthor,]
publication_author_df = pd.merge(authorOnTable, publication_author, on='id_author')
listPubliAuthor = pd.merge(publication_author_df, publication, on='id_publication')
print(listPubliAuthor.article_title.values)

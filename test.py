import pandas as pd

author = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/author.csv", engine='python', error_bad_lines=False)
keyword = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/keyword.csv", engine='python', error_bad_lines=False)
publication = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication.csv", engine='python', error_bad_lines=False)
publication_author = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_author.csv", engine='python', error_bad_lines=False)
publication_keyword = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_keywords.csv", engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_venue.csv", engine='python', error_bad_lines=False)
publication_year = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/publication_year.csv", engine='python', error_bad_lines=False)
venue = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/venue.csv", engine='python', error_bad_lines=False)
year = pd.read_csv("C:/Users/annes/OneDrive/cours/Master 1/Projet/dataset/year.csv", engine='python', error_bad_lines=False)

print(author.loc[author.name_author=='A. Andersson',])

print("*Liste de toutes les publications d'un auteur*")
nameAuthor = input("Entrez le nom d'un auteur : ")
authorOnTable = author.loc[author.name_author==nameAuthor,]
publication_author_df = pd.merge(authorOnTable, publication_author, on='id_author')
listPubliAuthor = pd.merge(publication_author_df, publication, on='id_publication')
print(listPubliAuthor.article_title.values)


print("*Liste de tous les co-auteurs d'une publication*")
namePubli = input("Entrez le titre d'une publication : ")
publiOnTable = publication.loc[publication.article_title==namePubli,]
publication_author_df = pd.merge(publiOnTable, publication_author, on='id_publication')
listPubliAuthor = pd.merge(publication_author_df, author, on='id_author')
print(listPubliAuthor.name_author.values)


print("*Liste des keywords d'une publication*")
namePubli = input("Entrez le titre d'une publication : ")
publiOnTable = publication.loc[publication.article_title==namePubli,]
publication_keywords_df = pd.merge(publiOnTable, publication_keyword, on='id_publication')
listKeywordPublic = pd.merge(publication_keywords_df, keyword, on='keyword')['keyword']
print(listKeywordPublic.values)


#etiquette = {name_author,nbr_publication, date_pub,nbr_authors,article_title,categorie}


print("*Liste des x de y*")
y = input("Entrez l'objet de votre recherche (nom d'une publication, nom d'un auteur, nom d'un évènement...'): ")
objcat = input("Entrez le nom de la varible que vous cherchez (si c'est le nom d'un auteur, c'est name_author par ex) :")
obj = input("Entrez la catégorie de cet objet (publication, author, keyword, venue) :")
x = input("Entrez l'étiquette de la liste que vous voulez afficher (name_author, article_title, keyword...) : ")
objx = input("Entrez la catégorie de cet objet (publication, author, keyword, venue) :")
etiquette={'article_title':donnees[obj].article_title==y} #uniquement pour un nom d'article pour l'instant
onTable = donnees[obj].loc[etiquette[objcat],]
dfMerge = pd.merge(onTable, publication_keyword, on='id_publication')
listEnd = (pd.merge(dfMerge, donnees[objx], on=x))[objx]
print(listEnd.values)


#création de la requete dynamique
donneesTable = {'author': author, 'publication': publication, 'venue':venue, 'keyword':keyword}
idTable = {'author': publication_author, 'publication': publication, 'venue':publication_venue, 'keyword':publication_keyword}
idName = {'author': 'id_author', 'publication': 'id_publication', 'venue':'id_venue', 'keyword':'keyword'}
    #name : nom de la cible (centre du graphe)
    #typename : type de la cible (author, publication, keyword...)
    #att1, att2, att3 : attribut aux niveau 1, 2 et 3 du graphe
    #typeAtt1, typeAtt2, typeAtt3 : type de ces attributs
def request(name, typename, att1, typeAtt1, att2, typeAtt2, att3, typeAtt3):
    if typename=="author":
        table = author.loc[author.name_author==name,]
    elif typename=="publication":
        table = publication.loc[publication.article_title==name,]
    elif typename == "keyword":
        table = keyword.loc[keyword.keyword==name,]
    elif typename == "venue":
        table = venue.loc[venue.name_venue==name,]
    else:
        return "Erreur : le type d'entrée n'existe pas"
    
    if att1 != "":
        if typeAtt1!="publication":
            table = pd.merge(table, idTable[typeAtt1], on='id_publication')
        
        table = pd.merge(table, donneesTable[typeAtt1],on=idName[typeAtt1])[att1]
        
    print(table.values)


#request("'Yinka Oyerinde", "author", "article_title","publication","","","","")
request("FEATS: Synthetic Feature Tracks for Structure from Motion Evaluation.","publication","name_author","author","","","","")

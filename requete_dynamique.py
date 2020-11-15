# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:33:45 2020

@author: david
"""
import pandas as pd
from tkinter import Tk,Label,Button, Entry,IntVar,Checkbutton

#importation fichiers CSV
author = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
keyword = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/keyword.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication.csv", engine='python', error_bad_lines=False, warn_bad_lines=False)
publication_author = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_keywords = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_keywords.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
publication_year = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
venue = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
year = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)



#requete dynamique
donneesTable = {'author': author, 'publication': publication, 'venue':venue, 'keyword':keyword, 'year':year}
idTable = {'author': publication_author, 'publication': publication, 'venue':publication_venue, 'keyword':publication_keywords, 'year':publication_year}
idName = {'author': 'id_author', 'publication': 'id_publication', 'venue':'id_venue', 'keyword':'keyword', 'year': 'id_year'}
    #name : nom de la cible (centre du graphe)
    #typename : type de la cible (author, publication, keyword, venue)
    #attribute : liste d'attributs à afficher
    #typeAtt : ensemble des types de ces attributs
def request(name, typename, attribute, typeAtt):
    if typename=="author":
        table = author.loc[author.name_author==name,]
    elif typename=="publication":
        table = publication.loc[publication.article_title==name,]
    elif typename == "keyword":
        table = keyword.loc[keyword.keyword==name,]
    elif typename == "venue":
        table = venue.loc[venue.name_venue==name,]
    elif typename == "year":
        table = year.loc[year.year==int(name),]
    else:
        return "Erreur : le type d'entrée n'existe pas"
    table = pd.merge(table, idTable[typename], on=idName[typename])
    typeAtt.discard(typename)
    for typ in typeAtt:
        if typ!="publication":
            table = pd.merge(table, idTable[typ], on='id_publication') 
        table = pd.merge(table, donneesTable[typ],on=idName[typ])

    return table[attribute].values


####Fonction qui gère les selections de l'utilisateur
def btn_entree_clic_Publi():
    name = ZonedeT_publi.get()
    typename = "publication"
    att=[]
    typeAtt = set()
    if Nom_Auteur_val.get() == 1 :
        att.append("name_author")
        typeAtt.add("author")
    if NamePubli_val.get() == 1 :
        att.append("article_title")
        typeAtt.add("publication")
    if date_publication.get() == 1:
        att.append("date_pub")
        typeAtt.add("publication")
    if ListeKeyword_val.get() == 1:
        att.append("keyword")
        typeAtt.add("keyword")
    if lieu_publi_val.get()== 1:
        att.append("name_venue")
        typeAtt.add("venue")
    if T_lieu_publi_val.get()==1:
        att.append("type_venue")
        typeAtt.add("venue")
    if categorie_val.get()== 1:
        att.append("categorie")
        typeAtt.add("publication")
    if choix_annee.get()== 1:
        att.append("year")
        typeAtt.add("year")
    print(request(name, typename, att, typeAtt))


def btn_entree_clic_Auteur():
    name = ZonedeT_author.get()
    typename = "author"
    att=[]
    typeAtt = set()
    if Nom_Auteur_val.get() == 1 :
        att.append("name_author")
        typeAtt.add("author")
    if NamePubli_val.get() == 1 :
        att.append("article_title")
        typeAtt.add("publication")
    if date_publication.get() == 1:
        att.append("date_pub")
        typeAtt.add("publication")
    if ListeKeyword_val.get() == 1:
        att.append("keyword")
        typeAtt.add("keyword")
    if lieu_publi_val.get()== 1:
        att.append("name_venue")
        typeAtt.add("venue")
    if T_lieu_publi_val.get()==1:
        att.append("type_venue")
        typeAtt.add("venue")
    if categorie_val.get()== 1:
        att.append("categorie")
        typeAtt.add("publication")
    print(request(name, typename, att, typeAtt))
    
def btn_entree_clic_Keyword():
    name = ZonedeT_keyword.get()
    typename = "keyword"
    att=[]
    typeAtt = set()
    if Nom_Auteur_val.get() == 1 :
        att.append("name_author")
        typeAtt.add("author")
    if NamePubli_val.get() == 1 :
        att.append("article_title")
        typeAtt.add("publication")
    if date_publication.get() == 1:
        att.append("date_pub")
        typeAtt.add("publication")
    if ListeKeyword_val.get() == 1:
        att.append("keyword")
        typeAtt.add("keyword")
    if lieu_publi_val.get()== 1:
        att.append("name_venue")
        typeAtt.add("venue")
    if T_lieu_publi_val.get()==1:
        att.append("type_venue")
        typeAtt.add("venue")
    if categorie_val.get()== 1:
        att.append("categorie")
        typeAtt.add("publication")
    print(request(name, typename, att, typeAtt))
    
def btn_entree_clic_Venue():
    name = ZonedeT_venue.get()
    typename = "venue"
    att=[]
    typeAtt = set()
    if Nom_Auteur_val.get() == 1 :
        att.append("name_author")
        typeAtt.add("author")
    if NamePubli_val.get() == 1 :
        att.append("article_title")
        typeAtt.add("publication")
    if date_publication.get() == 1:
        att.append("date_pub")
        typeAtt.add("publication")
    if ListeKeyword_val.get() == 1:
        att.append("keyword")
        typeAtt.add("keyword")
    if lieu_publi_val.get()== 1:
        att.append("name_venue")
        typeAtt.add("venue")
    if T_lieu_publi_val.get()==1:
        att.append("type_venue")
        typeAtt.add("venue")
    if categorie_val.get()== 1:
        att.append("categorie")
        typeAtt.add("publication")
    print(request(name, typename, att, typeAtt))

def btn_entree_clic_Year():
    name = ZonedeT_year.get()
    typename = "year"
    att=[]
    typeAtt = set()
    if Nom_Auteur_val.get() == 1 :
        att.append("name_author")
        typeAtt.add("author")
    if NamePubli_val.get() == 1 :
        att.append("article_title")
        typeAtt.add("publication")
    if date_publication.get() == 1:
        att.append("date_pub")
        typeAtt.add("publication")
    if ListeKeyword_val.get() == 1:
        att.append("keyword")
        typeAtt.add("keyword")
    if lieu_publi_val.get()== 1:
        att.append("name_venue")
        typeAtt.add("venue")
    if T_lieu_publi_val.get()==1:
        att.append("type_venue")
        typeAtt.add("venue")
    if categorie_val.get()== 1:
        att.append("categorie")
        typeAtt.add("publication")
    print(request(name, typename, att, typeAtt))

###################################         INTERFACE UTILISATEUR      ######################################  

##### Fenetre principale avec ces ca3D-GISractéristiques
fenetre = Tk()
fenetre.geometry('565x460')
#fenetre.configure(bg='grey')
#fenetre['bg'] = '#2ecc71'
fenetre.title("Recherche utilisateur")

#####Titre des inputbox
label_publi = Label(fenetre, text="Nom publication : ",fg = "orange",font = ("Arial", 10 , "bold"))
label_publi.grid(row=0,column=0)

label_author = Label(fenetre, text="Nom auteur : ",fg = "orange",font = ("Arial", 10, "bold"))
label_author.grid(row=1,column=0)

label_keyword = Label(fenetre, text="Keyword : ",fg = "orange",font = ("Arial", 10, "bold"))
label_keyword.grid(row=2,column=0)

label_venue = Label(fenetre, text="Lieu : ",fg = "orange",font = ("Arial", 10, "bold"))
label_venue.grid(row=3,column=0)
fenetre.grid_rowconfigure(4, minsize=20)

label_year = Label(fenetre, text="Année : ",fg = "orange",font = ("Arial", 10, "bold"))
label_year.grid(row=4,column=0)
fenetre.grid_rowconfigure(5, minsize=20)


##### Zone de texte pour les publications / Auteurs / Keyword
#Entrée de mots_clefs et nom
ZonedeT_publi = Entry(fenetre, width=30)
ZonedeT_publi.grid(row=0,column=1)

ZonedeT_author = Entry(fenetre, width=30)
ZonedeT_author.grid(row=1,column=1)

ZonedeT_keyword = Entry(fenetre, width=30)
ZonedeT_keyword.grid(row=2,column=1)

ZonedeT_venue = Entry(fenetre, width=30)
ZonedeT_venue.grid(row=3,column=1)

ZonedeT_year = Entry(fenetre, width=30)
ZonedeT_year.grid(row=4,column=1)

#Filtres
#####Boutons pour la table AUTEUR
Filtres_aut = Label(fenetre, text="Attributs AUTEUR :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_aut.grid(row=6,column=0)
Nom_Auteur_val = IntVar()
chk_btn_nomAuteur = Checkbutton(fenetre, text="Nom_Auteur", variable=Nom_Auteur_val,font = ("Arial", 9))
chk_btn_nomAuteur.grid(row=7,column=0)


#####Boutons pour la table KEYWORD
Filtres_keyword = Label(fenetre, text="Attributs KEYWORD :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_keyword.grid(row=9,column=0)
ListeKeyword_val = IntVar()
chk_btn_ListeK = Checkbutton(fenetre, text="Nom_Keyword", variable=ListeKeyword_val,font = ("Arial", 9 ))
chk_btn_ListeK.grid(row=10,column=0)
fenetre.grid_rowconfigure(8, minsize=10)


##### Boutons sur les années souahitée
Filtres_annee = Label(fenetre, text="Attributs YEAR :",fg = "orange",font = ("Arial", 10 , "bold") )
Filtres_annee.grid(row=12,column=0)
choix_annee = IntVar()
annee = Checkbutton(fenetre, text="Nom_Annee", variable=choix_annee,font = ("Arial", 9))
annee.grid(row=13,column=0)
fenetre.grid_rowconfigure(11, minsize=10)


#####Boutons pour la table VENUE
Filtres_Lieu = Label(fenetre, text="Attributs VENUE :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_Lieu.grid(row=14,column=0)
lieu_publi_val = IntVar()
chk_btn_lieu = Checkbutton(fenetre, text="Nom_Lieu", variable=lieu_publi_val,font = ("Arial", 9))
chk_btn_lieu.grid(row=15,column=0)

T_lieu_publi_val = IntVar()
chk_btn_T_lieu = Checkbutton(fenetre, text="Type_Lieu", variable=T_lieu_publi_val,font = ("Arial", 9))
chk_btn_T_lieu.grid(row=15,column=1)
fenetre.grid_rowconfigure(16, minsize=10)


#####Boutons pour la table Publication
Filtres_publi = Label(fenetre, text="Attributs PUBLICATION :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_publi.grid(row=17,column=0)
NamePubli_val = IntVar()
chk_btn_NameP = Checkbutton(fenetre, text="Nom_Publication", variable=NamePubli_val,font = ("Arial", 9))
chk_btn_NameP.grid(row=18,column=0)

categorie_val = IntVar()
chk_btn_categorie = Checkbutton(fenetre, text="Categorie", variable=categorie_val,font = ("Arial", 9))
chk_btn_categorie.grid(row=18,column=1)

date_publication = IntVar()
date_Pu = Checkbutton(fenetre, text="Date_Publication", variable=date_publication,font = ("Arial", 9))
date_Pu.grid(row=18,column=3)
fenetre.grid_rowconfigure(19, minsize=10)

##### Boutons d'entrees de valeurs
btn_entree_publi=Button(fenetre, text="Valider", command=btn_entree_clic_Publi)
btn_entree_publi.grid(row=0,column=2)

btn_entree_author=Button(fenetre, text="Valider", command=btn_entree_clic_Auteur)
btn_entree_author.grid(row=1,column=2)

btn_entree_keyword=Button(fenetre, text="Valider", command=btn_entree_clic_Keyword)
btn_entree_keyword.grid(row=2,column=2)

btn_entree_venue=Button(fenetre, text="Valider", command=btn_entree_clic_Venue)
btn_entree_venue.grid(row=3,column=2)

btn_entree_year=Button(fenetre, text="Valider", command=btn_entree_clic_Year)
btn_entree_year.grid(row=4,column=2)

##### Boutons QUITTER
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.grid(row=20,column=8)

fenetre.mainloop()

#exemple de numero de publi : conf/3dim/AbarghoueiB19
#Exemple de nom d'auteur : Sebastian Rudolph
#Exemple de nom de publication : Self Functional Maps.
#ºExemple de nom venue : 3D-GIS

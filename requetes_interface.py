# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:43:37 2020

@author: david
"""
####librairie pandas
import pandas as pd
from tkinter import Tk,Label,Button, Entry,Radiobutton,IntVar,Checkbutton

#Exemple de numero auteur : id_79/6633

####Fonction qui gère les selections de l'utilisateur
def getText_nameP ():
    identifiant= ZonedeT_publi.get()
    nameP= ZonedeT_publi.get()
    publication[publication["name_publication"] == nameP]
    publication[publication["id_identifiant"] == identifiant]

def getText_nameA ():
    identifiantA= ZonedeT_publi.get()
    nameA= ZonedeT_publi.get()
    author[author["name_author"] == nameA]
    author[author["id_author"] == identifiantA]

def getText_Keyword ():
    motclef = ZonedeT_publi.get()
    keyword[keyword["keyword"] == motclef]


 
#def getannee ():
#    annee= var_choix.get()
#    nbyear=Label(fenetre, text=pubyear[pubyear["year"] == annee].id_publication.count())
#    nbyear.pack()
 
def btn_entree_clic():
    if nbAuthor_val.get() == 1 :
        if choix_annee.get()== 0 :
            print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].id_author.count())
        elif choix_annee.get()== 2017 :
            print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].id_author.count())
        elif choix_annee.get()== 2018 :
            print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].id_author.count())
        elif choix_annee.get()== 2019 :
            print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].id_author.count())
        
    if nbAuthor_val.get() == 0 and choix_annee.get()== 0 :
        print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].name_author)
        
    if ListeAuteur_val.get() == 1 and choix_annee.get()== 0 and nbAuthor_val.get() == 0 :
        print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].name_author)
    if nbAuthor_val.get() == 1 and choix_annee.get()== 0 and ListeAuteur_val.get() == 1 :
        print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].id_author.count) 
    if ListeKeyword_val.get() == 1 and choix_annee.get()== 0 and nbAuthor_val.get() == 0 and ListeAuteur_val.get() == 0 :
        print(pubkeyword[pubkeyword["article_title"] == ZonedeT_publi.get()].keyword)
    if lieu_publi_val.get() == 1 and choix_annee.get()== 0 and  ListeAuteur_val.get() == 0 and nbAuthor_val.get() == 0 and ListeAuteur_val.get() == 0 :
        print("*Le nom du lieu de la publication*")
        print(pubyear[pubyear["article_title"] == ZonedeT_publi.get()].name_venue)
        
        
def btn_entree_clic2():
    if choix_annee.get()== 0 :
        print(pubauthor[pubauthor["name_author"] == ZonedeT_author.get()].article.title)
    if ListePubli_val.get() == 1 and choix_annee.get()== 0 :
        print(pubauthor[pubauthor["name_author"] == ZonedeT_author.get()].article_title)
               
def btn_entree_clic3():        
    if nbKeyword_val.get() == 1 and choix_annee.get()== 0 :
        print(pubkeyword[pubkeyword["keyword"] == ZonedeT_keyword.get()].keyword.count)

        
###################################         INTERFACE UTILISATEUR      ######################################  

##### Fenetre principale avec ces caractéristiques
fenetre = Tk()
fenetre.geometry('500x400')
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
fenetre.grid_rowconfigure(3, minsize=20)


##### Zone de texte pour les publications / Auteurs / Keyword
#Entrée de mots_clefs et nom
ZonedeT_publi = Entry(fenetre, width=30)
ZonedeT_publi.grid(row=0,column=1)

ZonedeT_author = Entry(fenetre, width=30)
ZonedeT_author.grid(row=1,column=1)

ZonedeT_keyword = Entry(fenetre, width=30)
ZonedeT_keyword.grid(row=2,column=1)


#Filtres
##### Boutons sur les années souahitée
Filtres_annee = Label(fenetre, text="Filtres YEAR :",fg = "orange",font = ("Arial", 10 , "bold") )
Filtres_annee.grid(row=4,column=0)
choix_annee = IntVar()
annee2017 = Radiobutton(fenetre, text="2017", variable=choix_annee, value="2017",font = ("Arial", 9))
annee2018 = Radiobutton(fenetre, text="2018", variable=choix_annee, value="2018",font = ("Arial", 9))
annee2019 = Radiobutton(fenetre, text="2019", variable=choix_annee, value="2019",font = ("Arial", 9))
annees = Radiobutton(fenetre, text="Toutes", variable=choix_annee, value="0",font = ("Arial", 9))
annee2017.grid(row=5,column=0)
annee2018.grid(row=5,column=1)
annee2019.grid(row=5,column=2)
annees.grid(row=5,column=3)

#####Boutons pour la table VENUE
Filtres_Lieu = Label(fenetre, text="Filtres VENUE :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_Lieu.grid(row=7,column=0)
lieu_publi_val = IntVar()
chk_btn_lieu = Checkbutton(fenetre, text="lieu", variable=lieu_publi_val,font = ("Arial", 9))
chk_btn_lieu.grid(row=8,column=0)
fenetre.grid_rowconfigure(6, minsize=10)

#####Boutons pour la table AUTEUR
Filtres_aut = Label(fenetre, text="Filtres AUTEUR :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_aut.grid(row=10,column=0)
ListeAuteur_val = IntVar()
chk_btn_ListeA = Checkbutton(fenetre, text="Liste_Auteur", variable=ListeAuteur_val,font = ("Arial", 9))
chk_btn_ListeA.grid(row=11,column=1)

nbAuthor_val = IntVar()
chk_btn_nbAuthor = Checkbutton(fenetre, text="Nb_Author", variable=nbAuthor_val,font = ("Arial", 9))
chk_btn_nbAuthor.grid(row=11,column=0)
fenetre.grid_rowconfigure(9, minsize=10)

#####Boutons pour la table Publication
Filtres_publi = Label(fenetre, text="Filtres PUBLICATION :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_publi.grid(row=13,column=0)
ListePubli_val = IntVar()
chk_btn_ListeP = Checkbutton(fenetre, text="Liste_Publication", variable=ListePubli_val,font = ("Arial", 9))
chk_btn_ListeP.grid(row=14,column=1)

nbPubli_val = IntVar()
chk_btn_nbPubli = Checkbutton(fenetre, text="Nb_Publication", variable=nbPubli_val,font = ("Arial", 9))
chk_btn_nbPubli.grid(row=14,column=0)
fenetre.grid_rowconfigure(12, minsize=10)


#####Boutons pour la table KEYWORD
Filtres_keyword = Label(fenetre, text="Filtres KEYWORD :",fg = "orange",font = ("Arial", 10 , "bold"))
Filtres_keyword.grid(row=16,column=0)
ListeKeyword_val = IntVar()
chk_btn_ListeK = Checkbutton(fenetre, text="Liste_Keyword", variable=ListeKeyword_val,font = ("Arial", 9 ))
chk_btn_ListeK.grid(row=17,column=1)

nbKeyword_val = IntVar()
chk_btn_nbKeyword = Checkbutton(fenetre, text="Nb_Keyword", variable=nbKeyword_val,font = ("Arial", 9))
chk_btn_nbKeyword.grid(row=17,column=0)
fenetre.grid_rowconfigure(15, minsize=10)

##### Boutons d'entrees de valeurs
btn_entree_publi=Button(fenetre, text="Valider", command=btn_entree_clic)
btn_entree_publi.grid(row=0,column=2)

btn_entree_author=Button(fenetre, text="Valider", command=btn_entree_clic2)
btn_entree_author.grid(row=1,column=2)

btn_entree_keyword=Button(fenetre, text="Valider", command=btn_entree_clic3)
btn_entree_keyword.grid(row=2,column=2)

##### Boutons QUITTER
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.grid(row=18,column=8)


fenetre.mainloop()


###################################      Import des fichiers csv      ######################################
author = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
keyword = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/keyword.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication.csv", engine='python', error_bad_lines=False, warn_bad_lines=False)
publication_author = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_keywords = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_keywords.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
publication_year = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
venue = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
year = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)


###################################       Jointures      ######################################
#exemple de numero de publi : conf/3dim/AbarghoueiB19
#Exemple de nom d'auteur : Sebastian Rudolph
#Exemple de nom de publication : Self Functional Maps.

pubvenue = publication.merge(publication_venue, on="id_publication")
pubvenue = pubvenue.merge(venue, left_on="id_venue", right_on="id_venue")


pubauthor = pubvenue.merge(publication_author, how="inner", on="id_publication")
pubauthor = pubauthor.merge(author, how="inner", on="id_author")

pubyear = pubauthor.merge(publication_year, on="id_publication")
pubyear = pubyear.merge(year, left_on="id_year", right_on="id_year")

pubkeyword = pubyear.merge(publication_keywords, on="id_publication")
pubkeyword = pubkeyword.merge(year, left_on="keyword", right_on="keyword")

#resultat = pubyear.groupby('year').name_author.nunique()
#print(resultat)





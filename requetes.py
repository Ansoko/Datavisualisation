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
def getText ():
    identifiant= ZonedeT.get()
    name= ZonedeT.get()
    print(author[author["name_author"] == name])
    print(author[author["id_author"] == identifiant])
    
#def getannee ():
#    annee= var_choix.get()
#    nbyear=Label(fenetre, text=pubyear[pubyear["year"] == annee].id_publication.count())
#    nbyear.pack()
 
def btn_entree_clic():
    if nbAuthor_val.get() == 1 and choix_annee.get()== 0 :
        print(pubyear[pubyear["id_publication"] == ZonedeT.get()].id_author.count())
        #pubyear[pubyear["id_publication"] == ZonedeT.get()].id_author.count()
    if nbAuthor_val.get() == 1 and choix_annee.get()== 2017 :
        print(pubyear[pubyear["id_publication"] == ZonedeT.get()].id_author.count())
    if nbAuthor_val.get() == 1 and choix_annee.get()== 2018 :
        print(pubyear[pubyear["id_publication"] == ZonedeT.get()].id_author.count())
    if nbAuthor_val.get() == 1 and choix_annee.get()== 2019 :
        print(pubyear[pubyear["id_publication"] == ZonedeT.get()].id_author.count())
    if nbAuthor_val.get() == 0 and choix_annee.get()== 0 :
        print(pubyear[pubyear["id_publication"] == ZonedeT.get()].publication)
    
    

####INTERFACE UTILISATEUR    
# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.title("Recherche utilisateur")
label = Label(fenetre, text="Identfiant : ")
label.grid(row=0,column=0)

Filtres = Label(fenetre, text="Choix des filtres :")
Filtres.grid(row=1,column=0)

choix_annee = IntVar()
annee2017 = Radiobutton(fenetre, text="2017", variable=choix_annee, value="2017")
annee2018 = Radiobutton(fenetre, text="2018", variable=choix_annee, value="2018")
annee2019 = Radiobutton(fenetre, text="2019", variable=choix_annee, value="2019")
annees = Radiobutton(fenetre, text="toutes", variable=choix_annee, value="0")
annee2017.grid(row=2,column=0)
annee2018.grid(row=3,column=0)
annee2019.grid(row=4,column=0)
annees.grid(row=5,column=0)

ZonedeT = Entry(fenetre, width=30)
ZonedeT.grid(row=0,column=6)

nbAuthor_val = IntVar()
chk_btn_nbpubli = Checkbutton(fenetre, text="nb_Author", variable=nbAuthor_val)
chk_btn_nbpubli.grid(row=6,column=0)


btn_entree=Button(fenetre, text="Entrée", command=btn_entree_clic)
btn_entree.grid(row=6,column=7)

#Boutons QUITTER
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.grid(row=6,column=8)
fenetre.mainloop()
#


####import des fichiers csv
author = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
# keyword = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/keyword.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication.csv", engine='python', error_bad_lines=False, warn_bad_lines=False)
publication_author = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_author.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
# publication_keywords = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_keywords.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
publication_venue = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
publication_year = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/publication_year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)
venue = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/venue.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False, warn_bad_lines=False)
year = pd.read_csv("C:/Users/david/OneDrive/Bureau/Master informatique/Semestre 7/Projet intégré/Dataset/year.csv", encoding= 'unicode_escape', engine='python', error_bad_lines=False)


########### REQUETES #################

#Requete le lieu de la publication 
#exemple de numero de publi : conf/3dim/AbarghoueiB19
#
#print("*Le nom du lieu d'une publication*")
#noPubli = input("Entrez l'id de la publication : ")
pubvenue = publication.merge(publication_venue, on="id_publication")
pubvenue = pubvenue.merge(venue, left_on="id_venue", right_on="id_venue")
##print(pubvenue[pubvenue["id_publication"] == noPubli].name_venue)
#
#
#print("*Le nombre d'auteurs différents ayant fait une publication par année*")
pubauthor = pubvenue.merge(publication_author, how="inner", on="id_publication")
pubauthor = pubauthor.merge(author, how="inner", on="id_author")
pubyear = pubauthor.merge(publication_year, on="id_publication")
pubyear = pubyear.merge(year, left_on="id_year", right_on="id_year")
#
#resultat = pubyear.groupby('year').name_author.nunique()
#print(resultat)

#pubauthor = publication.merge(publication_author, how="inner", on="id_publication")
#pubauthor = pubauthor.merge(author, how="inner", on="id_author")





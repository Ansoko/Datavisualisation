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
    if (typename != 'publication'):
        typeAtt.discard(typename)
    for typ in typeAtt:
        if typ!="publication":
            table = pd.merge(table, idTable[typ], on='id_publication') 
        table = pd.merge(table, donneesTable[typ],on=idName[typ])

    return table[attribute].values


#Fonction déclenchée par le bouton valider. Va lancer la recherche sur le 1er champ rempli
def btn_entree_valider():
    if ZonedeT_publi.get():
        Lancer_Recherche_Sur_Publi() 
    elif ZonedeT_author.get():
        Lancer_Recherche_Sur_Auteur() 
    elif ZonedeT_keyword.get():
        Lancer_Recherche_Sur_Keyword()
    elif ZonedeT_venue.get():
        Lancer_Recherche_Sur_Venue()
    elif ZonedeT_year.get():
        Lancer_Recherche_Sur_Year()
        
        
#fonction qui permet remplir les parametres att et typeAtt selon le choix de l'user dans l'interface
def set_att_typeAtt_from_intf(att,typeAtt):
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

 ####Fonction qui gère les selections de l'utilisateur   
def Lancer_Recherche_Sur_Publi():
    name = ZonedeT_publi.get()
    typename = "publication"
    att=[]
    typeAtt = set()
    set_att_typeAtt_from_intf(att, typeAtt)
    print(request(name, typename, att, typeAtt))

def Lancer_Recherche_Sur_Auteur():
    name = ZonedeT_author.get()
    typename = "author"
    att=[]
    typeAtt = set()
    set_att_typeAtt_from_intf(att, typeAtt)
    
    # att=[]
    # typeAtt = set()
    # if Nom_Auteur_val.get() == 1 :
    #     att.append("name_author")
    #     typeAtt.add("author")
    # if NamePubli_val.get() == 1 :
    #     att.append("article_title")
    #     typeAtt.add("publication")
    # if date_publication.get() == 1:
    #     att.append("date_pub")
    #     typeAtt.add("publication")
    # if ListeKeyword_val.get() == 1:
    #     att.append("keyword")
    #     typeAtt.add("keyword")
    # if lieu_publi_val.get()== 1:
    #     att.append("name_venue")
    #     typeAtt.add("venue")
    # if T_lieu_publi_val.get()==1:
    #     att.append("type_venue")
    #     typeAtt.add("venue")
    # if categorie_val.get()== 1:
    #     att.append("categorie")
    #     typeAtt.add("publication")
    print(request(name, typename, att, typeAtt))
    
def Lancer_Recherche_Sur_Keyword():
    name = ZonedeT_keyword.get()
    typename = "keyword"
    att=[]
    typeAtt = set()
    set_att_typeAtt_from_intf(att, typeAtt)
    print(request(name, typename, att, typeAtt))
    
def Lancer_Recherche_Sur_Venue():
    name = ZonedeT_venue.get()
    typename = "venue"
    att=[]
    typeAtt = set()
    set_att_typeAtt_from_intf(att, typeAtt)
    print(request(name, typename, att, typeAtt))

def Lancer_Recherche_Sur_Year():
    name = ZonedeT_year.get()
    typename = "year"
    att=[]
    typeAtt = set()
    set_att_typeAtt_from_intf(att, typeAtt)
    print(request(name, typename, att, typeAtt))

###################################         INTERFACE UTILISATEUR      ######################################  

##### Fenetre principale avec ces caractéristiques
fenetre = Tk()
fenetre.geometry('620x530')
#fenetre.configure(bg='grey')
#fenetre['bg'] = '#2ecc71'
fenetre.title("Recherche utilisateur")

#####Titre des inputbox
label_publi = Label(fenetre, text="Titre publication  ",fg = "DodgerBlue4",font = ("Arial", 10 , "bold"))
label_publi.grid(row=1,column=0)

label_author = Label(fenetre, text="Nom auteur  ",fg = "DodgerBlue4",font = ("Arial", 10, "bold"))
label_author.grid(row=2,column=0)

label_keyword = Label(fenetre, text="Mot-clé  ",fg = "DodgerBlue4",font = ("Arial", 10, "bold"))
label_keyword.grid(row=3,column=0)

label_venue = Label(fenetre, text="Lieu  ",fg = "DodgerBlue4",font = ("Arial", 10, "bold"))
label_venue.grid(row=4,column=0)

label_year = Label(fenetre, text="Année  ",fg = "DodgerBlue4",font = ("Arial", 10, "bold"))
label_year.grid(row=5,column=0)
fenetre.grid_rowconfigure(6, minsize=10)

Indic_crit = Label(fenetre, text="Taper ce que vous souahitez chercher ",fg = "red2",font = ("Arial", 9 , "bold"))
Indic_crit.grid(row=0,column=0)


Indic_uti = Label(fenetre, text="Choisisser ce que vous voulez afficher  ",fg = "red2",font = ("Arial", 9 , "bold"))
Indic_uti.grid(row=8,column=0)
Indic_uti = Label(fenetre, text="en cochant les cases ci-dessous  ",fg = "red2",font = ("Arial", 9 , "bold"))
Indic_uti.grid(row=9,column=0)
fenetre.grid_rowconfigure(7, minsize=10)

##### Zone de texte pour les publications / Auteurs / Keyword
#Entrée de mots_clefs et nom
ZonedeT_publi = Entry(fenetre, width=30)
ZonedeT_publi.grid(row=1,column=1)

ZonedeT_author = Entry(fenetre, width=30)
ZonedeT_author.grid(row=2,column=1)

ZonedeT_keyword = Entry(fenetre, width=30)
ZonedeT_keyword.grid(row=3,column=1)

ZonedeT_venue = Entry(fenetre, width=30)
ZonedeT_venue.grid(row=4,column=1)

ZonedeT_year = Entry(fenetre, width=30)
ZonedeT_year.grid(row=5,column=1)

#Filtres
#####Boutons pour la table AUTEUR
Filtres_aut = Label(fenetre, text="Attributs AUTEUR ",fg = "DodgerBlue4",font = ("Arial", 9 , "bold"))
Filtres_aut.grid(row=10,column=0)
Nom_Auteur_val = IntVar()
chk_btn_nomAuteur = Checkbutton(fenetre, text="Nom de l'Auteur", variable=Nom_Auteur_val,font = ("Arial", 9))
chk_btn_nomAuteur.grid(row=11,column=0)


#####Boutons pour la table KEYWORD
Filtres_keyword = Label(fenetre, text="Attributs KEYWORD ",fg = "DodgerBlue4",font = ("Arial", 9 , "bold"))
Filtres_keyword.grid(row=13,column=0)
ListeKeyword_val = IntVar()
chk_btn_ListeK = Checkbutton(fenetre, text="Mots clés", variable=ListeKeyword_val,font = ("Arial", 9 ))
chk_btn_ListeK.grid(row=14,column=0)
fenetre.grid_rowconfigure(12, minsize=10)


##### Boutons sur les années souahitée
Filtres_annee = Label(fenetre, text="Attributs YEAR ",fg = "DodgerBlue4",font = ("Arial", 9 , "bold") )
Filtres_annee.grid(row=16,column=0)
choix_annee = IntVar()
annee = Checkbutton(fenetre, text="Nom de l'Annee", variable=choix_annee,font = ("Arial", 9))
annee.grid(row=17,column=0)
fenetre.grid_rowconfigure(15, minsize=10)


#####Boutons pour la table VENUE
Filtres_Lieu = Label(fenetre, text="Attributs VENUE ",fg = "DodgerBlue4",font = ("Arial", 9 , "bold"))
Filtres_Lieu.grid(row=19,column=0)
lieu_publi_val = IntVar()
chk_btn_lieu = Checkbutton(fenetre, text="Nom du Lieu", variable=lieu_publi_val,font = ("Arial", 9))
chk_btn_lieu.grid(row=20,column=0)

T_lieu_publi_val = IntVar()
chk_btn_T_lieu = Checkbutton(fenetre, text="Type du Lieu", variable=T_lieu_publi_val,font = ("Arial", 9))
chk_btn_T_lieu.grid(row=20,column=1)
fenetre.grid_rowconfigure(18, minsize=10)


#####Boutons pour la table Publication
Filtres_publi = Label(fenetre, text="Attributs PUBLICATION ",fg = "DodgerBlue4",font = ("Arial", 9 , "bold"))
Filtres_publi.grid(row=22,column=0)
NamePubli_val = IntVar()
chk_btn_NameP = Checkbutton(fenetre, text="Titre de la Publication", variable=NamePubli_val,font = ("Arial", 9))
chk_btn_NameP.grid(row=23,column=0)

categorie_val = IntVar()
chk_btn_categorie = Checkbutton(fenetre, text="Categorie de la Publication ", variable=categorie_val,font = ("Arial", 9))
chk_btn_categorie.grid(row=23,column=1)

date_publication = IntVar()
date_Pu = Checkbutton(fenetre, text="Date de la Publication", variable=date_publication,font = ("Arial", 9))
date_Pu.grid(row=23,column=3)
fenetre.grid_rowconfigure(21, minsize=10)
fenetre.grid_rowconfigure(24, minsize=10)
##### Boutons d'entrees de valeurs
btn_valider=Button(fenetre, text="Valider", command=btn_entree_valider)
btn_valider.grid(row=26,column=8)


##### Boutons QUITTER
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.grid(row=25,column=8)

fenetre.mainloop()

#exemple de numero de publi : conf/3dim/AbarghoueiB19
#Exemple de nom d'auteur : Sebastian Rudolph
#Exemple de nom de publication : Self Functional Maps.
#ºExemple de nom venue : 3D-GIS

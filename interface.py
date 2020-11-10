# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:19:50 2020

@author: Nico
"""

from tkinter import *
from tkcalendar import Calendar,DateEntry
from tk_html_widgets import HTMLLabel



def effacer():
    Champ.delete(0,END)
    Champ2.delete(0,END)
    Champ3.delete(0,END)
    Champ4.delete(0,END)
    Champ5.delete(0,END)
    Champ6.delete(0,END)
    Champ7.delete(0,END)
    C1.deselect()
    C2.deselect()
    C3.deselect()
    C4.deselect()
    C5.deselect()
    C6.deselect()
    homme.deselect()
    femme.deselect()
 
def envoyer():
 
    if (sex.get()==1):
        x="Mr"
    elif (sex.get()==2):
        x="Mme"
 
    aa=""
    bb=""
    cc=""
    dd=""
    ee=""
    ff=""    
  
     
fenetre= Tk()
fenetre.geometry("1080x720")
fenetre.minsize(1080,720)
fenetre.maxsize(1080,720)
fenetre.config(background='#2ecc71') 

#Menu 
menu_bar = Menu(fenetre)

#creer un menu 

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Nouveau")
file_menu.add_command(label="Quitter",command=fenetre.quit())
menu_bar.add_cascade(label="Fichier",menu=file_menu)

fenetre.config(menu=menu_bar)

#Formulaire

#Recherche d'auteur
Titre = Label(fenetre, text="Welcome to DataViz 2 Application", font=("Courrier",20))
Titre.place(x=360,y=10)
Nom = Label(fenetre, text = 'Nom Auteur: ')
Nom.grid(column=1, row=1, sticky='n',pady=(100,2),padx=(350,0))
Nom=StringVar()
Champ = Entry(fenetre, textvariable= Nom, width=31)
Champ.grid(column=2, row=1, columnspan=2,pady=(100,2))
 
Nombre_Publication = Label(fenetre, text = 'Nombre de publication : ')
Nombre_Publication.grid(column=1, row=2,sticky='n',pady=(2,2),padx=(350,0))
Nombre_Publication=StringVar()
Champ2 = Entry(fenetre, textvariable= Nombre_Publication, width=31)
Champ2.grid(column=2, row=2,columnspan=2)
 
#Recherche Publication
 
keywords = Label(fenetre, text = 'Mots Clés : ')
keywords.grid(column=1, row=3, sticky='n',pady=(200,2),padx=(350,0))
keywords=StringVar()
Champ3 = Entry(fenetre, textvariable= keywords,width=31)
Champ3.grid(column=2, row=3,columnspan=2,pady=(200,2))
 
 
category = Label(fenetre, text = 'Categorie : ')
category.grid(column=1, row=4,sticky='n',pady=2,padx=(350,0))
category=StringVar()
Champ4 = Entry(fenetre, textvariable= category,width=31)
Champ4.grid(column=2, row=4,columnspan=2)
 
 
date_publication = Label(fenetre, text = 'Date Publication : ')
date_publication.grid(column=1, row=5,sticky='n', pady=2,padx=(350,0))
date_publication=StringVar()
Champ5 = DateEntry(fenetre, textvariable= date_publication,width=31)
Champ5.grid(column=2, row=5,columnspan=2)
 
 
year = Label(fenetre, text = 'Annee : ')
year.grid(column=1, row=6, sticky='n',pady=2)
year=StringVar()
Champ6 =  OptionMenu(fenetre,year,'2020','2019','2018','2017')
Champ6.grid(column=2, row=6,columnspan=2)

"""
homme= Radiobutton (fenetre, text="homme", variable=sex, value=1)
homme.grid(column=1, row=7,sticky='sw')
femme= Radiobutton (fenetre, text="femme", variable=sex, value=2)
femme.grid(column=2, row=7,sticky='sw')
 
 
Hobbies = Label(fenetre, text = 'Hobbies : ')
Hobbies.grid(column=0,row=9, sticky='w',pady=2)
 
 
c=IntVar()
e=IntVar()
p=IntVar()
m=IntVar()
t=IntVar()
r=IntVar()
 
C1= Checkbutton (text="Cinema", variable=c, onvalue=1, offvalue=0)
C1.grid (column=1, row=8,sticky='sw')
 
C2= Checkbutton (text="Equitation", variable=e, onvalue=2, offvalue=0)
C2.grid (column=1, row=9, sticky='sw')
 
C3= Checkbutton (text="Planche à voile", variable=p, onvalue=3, offvalue=0)
C3.grid (column=1, row=10, sticky='sw')
 
C4= Checkbutton (text="Musique", variable=m, onvalue=4, offvalue=0)
C4.grid (column=2, row=8,sticky='sw')
 
C5= Checkbutton (text="Theatre", variable=t, onvalue=5, offvalue=0)
C5.grid (column=2, row=9, sticky='sw')
 
C6= Checkbutton (text="Rien", variable=r, onvalue=6, offvalue=0)
C6.grid (column=2, row=10, sticky='sw')
"""
 
 
Envoyer= Button (fenetre, text="envoyer",command=envoyer, pady=2)
Envoyer.grid (column=1, row=11,sticky='n', pady=20)
Effacer= Button (fenetre, text="réinitialiser", command=effacer, pady=2)
Effacer.grid (column=2, row=11,sticky='n',pady=20)
              
fenetre.mainloop()

"""
window_app = Tk()
    
window_app.title('Interface DataViz 2')
window_app.geometry("1080x720")
window_app.minsize(1080,720)
window_app.maxsize(1080,720)
window_app.config(background='#2ecc71')

label_title = Label(window_app, text="Welcome to DataViz 2 Application", font=("Courrier",20))
label_title.place(x=360,y=10)

#Formulaire

#Recherche d'auteur
div = "<div id='author' background-color='red'>"
author_search = Label(text = "Recherche Auteur",width="20")

author_search.place(x=270,y=100)

name_author_label = Label(text="Nom Auteur")
publication_author_label = Label(text = "Nombre de publication")
name_author_label.place(x=270,y=130)
publication_author_label.place(x=270,y=190)

name_author = StringVar()
publication_author = IntVar()

name_author_entry = Entry(textvariable = name_author, width="30")
publication_author_entry = Entry(textvariable = publication_author, width="30")

name_author_entry.place(x=270,y=160)
publication_author_entry.place(x=270,y=220)
findiv = "</div>"
#Publication Filtre

publication_search = Label(text = "Recherche Publication" ,width="20")

publication_search.place(x=270,y=300)

keywords_label = Label(text="Mots Clés")
category_label = Label(text = "Catégorie")
date_publication_label = Label(text="Date de publication")
year_label = Label(text = "Année")
keywords_label.place(x=270,y=330)
category_label.place(x=270,y=390)
date_publication_label.place(x=270,y=450)
year_label.place(x=270,y=510)

keywords = StringVar()
category = StringVar()
year = IntVar()

date_publication = DateEntry(window_app,width=30,bg="darkblue",fg="white",year=2010)

date_publication.place(x=270,y=480)

keywords_entry = Entry(textvariable = keywords, width="30")
keywords_entry.place(x=270,y=360)
category.set('Aucune')
Category_select = OptionMenu(window_app,category,'test','test2')
Category_select.place(x=270,y=420)

year_entry =  OptionMenu(window_app,year,'2020','2019','2018','2017')
year_entry.place(x=270,y=540)
#Boutons de validation ou reset 
Envoyer= Button (window_app, text="rechercher")
Effacer= Button (window_app, text="réeinitialiser")
Envoyer.place(x=500,y=600)
Effacer.place(x=600,y=600)




#Menu 
menu_bar = Menu(window_app)

#creer un menu 

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Nouveau")
file_menu.add_command(label="Quitter",command=window_app.quit())
menu_bar.add_cascade(label="Fichier",menu=file_menu)

window_app.config(menu=menu_bar)

window_app.mainloop()
"""
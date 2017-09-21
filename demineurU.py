#!/usr/bin/env python
#-*- coding: utf-8 -*-

from random import *
import time
from Tkinter import *
from tkMessageBox import *




fenetre = Tk()
fenetre.title("Demineur")

global taille,niveau
taille = 10
niveau = 4


def game():
        
        
        if taille < 5:
                longueurCarre = 5

        else:
                longueurCarre = taille

        def cases():
                """ -> list[tuple(int,int,int)]
                On affecte aux cases les vaeulrs 0,1 ou 2 pour ensuite donner
                seulement a une valeur le role de mine"""
                #list_cases:list
                list_cases=[]
                for ligne in range(longueurCarre):
                    for colonne in range(longueurCarre):
                        valeur=randint(0,niveau)
                        list_cases.append((ligne,colonne,valeur))
                return list_cases

        def valeur_cases(list_cases):
                """ List[tuple(int,int,int)] -> dict{tuple(int,int):int}"""
                #on cree le dictionnaires avec les mines placee
                #cases: dict[tuple(int,int):bool]
                cases={}
                for ligne,colonne,valeur in list_cases:
                    if valeur < 1:
                        cases[(ligne,colonne)]=True      #ce sont des mines
                    else:
                        cases[(ligne,colonne)]=False     #ce ne sont pas des mines

                #on cree le dictionnaire avec les mines et la valeur  des cases
                #qui les touche
                #case_mines_val: list(int)
                case_mines_val = {}
                #on nomme L la largeur et longueur du terrain de jeu
                #L: int
                L = longueurCarre
                for ligne,colonne in cases:      
                    if cases[(ligne,colonne)]:
                        case_mines_val[(ligne,colonne)]="*"
                    else:
                        #nb cases represente le nb de mines a proximite de la case
                        #on verifie si les cases autour de celle qu on regarde existe
                        #et si cest des mines la valeur de la case augmente
                        nb_case=0
                        if ((ligne+1,colonne) in cases) and cases[(ligne+1,colonne)]:
                            nb_case+=1
                        if ((ligne-1,colonne) in cases) and cases[(ligne-1,colonne)]:
                            nb_case+=1
                        if ((ligne,colonne-1) in cases) and cases[(ligne,colonne-1)]:
                            nb_case+=1
                        if ((ligne,colonne+1) in cases) and cases[(ligne,colonne+1)]:
                            nb_case+=1
                        if ((ligne+1,colonne+1) in cases) and cases[(ligne+1,colonne+1)]:
                            nb_case+=1
                        if ((ligne+1,colonne-1) in cases) and cases[(ligne+1,colonne-1)]:
                            nb_case+=1
                        if ((ligne-1,colonne+1) in cases) and cases[(ligne-1,colonne+1)]:
                            nb_case+=1
                        if ((ligne-1,colonne-1) in cases) and cases[(ligne-1,colonne-1)]:
                            nb_case+=1
                        case_mines_val[(ligne,colonne)]=nb_case
                return case_mines_val

        def cachage_case():
                """ -> dict{tuple(int,int):str}
                on creer un dico du terrain de jeu mais cache"""
                #dict{tuple(int,int):str}
                case_cachee={}
                for ligne in range(longueurCarre):
                    for colonne in range(longueurCarre):
                        case_cachee[(ligne,colonne)]='  '
                return case_cachee

        list_cases = cases()
        case_mines_val = valeur_cases(list_cases)
        case_cachee = cachage_case()

        def fin(val_bool):
            if val_bool:
                    showinfo('Bien joue', 'GAGNE !\t')
            else:
                    for i in range(longueurCarre):
                       for j in range(longueurCarre):
                                if case_mines_val[(i,j)] == '*':
                                        button = Button(frame_button,text=case_mines_val[(i,j)],relief="sunken",bg="red").grid(row=i, column=j)
                                else:
                                        button = Button(frame_button,text=case_mines_val[(i,j)],relief="sunken").grid(row=i, column=j)
                    showerror("Defaite", "Perdu      ")
                    if askyesno('on se la refait', 'Voulez vous recommencer?'):
                        game()
                    else:
                        showwarning('', 'Tant pis...')
                        fenetre.destroy()
                        
                        
        def creusage_zero(ligne,colonne):
                """int*int-> bool
                on creuse toutes les cases autour des zeros"""
                case_cachee2 = case_cachee
                
                
                if (ligne+1<longueurCarre and colonne+1<longueurCarre) and (case_cachee2[(ligne+1,colonne+1)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne+1,colonne+1)],relief=SUNKEN).grid(row=ligne+1, column=colonne+1)
                        case_cachee2[(ligne+1,colonne+1)] = case_mines_val[(ligne+1,colonne+1)]
                        if case_mines_val[(ligne+1,colonne+1)] == 0:
                                creusage_zero(ligne+1,colonne+1)
                if (ligne+1<longueurCarre and colonne-1>=0) and (case_cachee2[(ligne+1,colonne-1)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne+1,colonne-1)],relief=SUNKEN).grid(row=ligne+1, column=colonne-1)
                        case_cachee2[(ligne+1,colonne-1)] = case_mines_val[(ligne+1,colonne-1)]
                        if case_mines_val[(ligne+1,colonne-1)] == 0:
                                creusage_zero(ligne+1,colonne-1)
                if (ligne+1<longueurCarre and colonne<longueurCarre) and (case_cachee2[(ligne+1,colonne)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne+1,colonne)],relief=SUNKEN).grid(row=ligne+1, column=colonne)
                        case_cachee2[(ligne+1,colonne)] = case_mines_val[(ligne+1,colonne)]
                        if case_mines_val[(ligne+1,colonne)] == 0:
                                creusage_zero(ligne+1,colonne)
                if (ligne-1>=0 and colonne+1<longueurCarre) and (case_cachee2[(ligne-1,colonne+1)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne-1,colonne+1)],relief=SUNKEN).grid(row=ligne-1, column=colonne+1)
                        case_cachee2[(ligne-1,colonne+1)] = case_mines_val[(ligne-1,colonne+1)]
                        if case_mines_val[(ligne-1,colonne+1)] == 0:
                                creusage_zero(ligne-1,colonne+1)
                if (ligne-1>=0 and colonne-1>=0) and (case_cachee2[(ligne-1,colonne-1)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne-1,colonne-1)],relief=SUNKEN).grid(row=ligne-1, column=colonne-1)
                        case_cachee2[(ligne-1,colonne-1)] = case_mines_val[(ligne-1,colonne-1)]
                        if case_mines_val[(ligne-1,colonne-1)] == 0:
                                creusage_zero(ligne-1,colonne-1)
                if (ligne-1>=0 and colonne<longueurCarre) and (case_cachee2[(ligne-1,colonne)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne-1,colonne)],relief=SUNKEN).grid(row=ligne-1, column=colonne)
                        case_cachee2[(ligne-1,colonne)] = case_mines_val[(ligne-1,colonne)]
                        if case_mines_val[(ligne-1,colonne)] == 0:
                                creusage_zero(ligne-1,colonne)
                if (ligne<longueurCarre and colonne+1<longueurCarre) and (case_cachee2[(ligne,colonne+1)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne,colonne+1)],relief=SUNKEN).grid(row=ligne, column=colonne+1)
                        case_cachee2[(ligne,colonne+1)] = case_mines_val[(ligne,colonne+1)]
                        if case_mines_val[(ligne,colonne+1)] == 0:
                                creusage_zero(ligne,colonne+1)
                if (ligne<longueurCarre and colonne-1>=0) and (case_cachee2[(ligne,colonne-1)] == '  '):
                        Button(frame_button,text=case_mines_val[(ligne,colonne-1)],relief=SUNKEN).grid(row=ligne, column=colonne-1)
                        case_cachee2[(ligne,colonne-1)] = case_mines_val[(ligne,colonne-1)]
                        if case_mines_val[(ligne,colonne-1)] == 0:
                                creusage_zero(ligne,colonne-1)
                #apres avoir verifier que ca ne sortait pas du cadre on propage
                
                
                
        def creuser(event):
                """dict{tuple(int,int):int}->
                on propose a lutilisateur de renter un tuple de son choix pour
                qu il voit si il y a une mine ou non"""
                #on modifie une copie
                case_cachee2 = case_cachee
                
                #dict de la position
                pos = event.widget.grid_info()
                
                ligne = int(pos['row'])
                colonne = int(pos['column'])
                

                #on prend les elements du tuple du dictionnaire
                case_cachee2[(ligne,colonne)] = case_mines_val[(ligne,colonne)]
                
                
                
                if case_cachee2[(ligne,colonne)]=='*':
                    return fin(0)  
                
                Button(frame_button,text=str(case_cachee2[(ligne,colonne)]),relief=SUNKEN).grid(row=ligne, column=colonne)

                #si on tombe sur un zero on propage le clic:
                if case_mines_val[(ligne,colonne)] == 0:
                        creusage_zero(ligne,colonne)
                        
                #if case_cachee2[(ligne+1,colonne)]=='@'  and case_mines_val[(ligne+1,colonne)] == '0' :
                #       return

                #on verifie que la partie n'est pas fini
                fin_game = True
                for ligne in range(longueurCarre):
                       for colonne in range(longueurCarre):
                               if case_cachee2[(ligne,colonne)] == "  ":
                                       if case_mines_val[(ligne,colonne)] != '*':
                                                fin_game = False
                if fin_game:
                        fin(1)
                return case_cachee2

        def poser_drapeau(event):
                """ ->
                fonction qui pose un drapeau la ou lutilsateur pense qu'il y a une mine"""
                #on modifie une copie
                case_cachee2 = case_cachee
                if event.widget["text"] == "M":
                    event.widget.config(text="  ",bg="gray85")
                    
                elif event.widget["relief"] != "sunken" :
                    
                    event.widget.config(text="M",bg="orange")
                
                return case_cachee2
        
        def affichage_plateau():
            global frame_button
            try :
                frame_button.destroy()
            except :
                    Exception
            frame_button = Frame(fenetre)
            frame_button.pack()
                    
            for i in range(longueurCarre):
               for j in range(longueurCarre):
                        button = Button(frame_button,text=str(case_cachee[(i,j)]))
                        button.grid(row=i, column=j)
                        fenetre.bind("<Button-3>",poser_drapeau)
                        fenetre.bind("<Button-1>",creuser)
            fenetre.resizable(0,0)
            
        affichage_plateau()

def alert():
    showinfo("alerte", "Bravo!")

def chg_taille(event):
        global taille
        taille = int(event)
        game()        

def scaletime():
        fenetre2 = Tk()
        fenetre2.title("taille")
        scale = Scale(fenetre2,from_=5,to=40,command=chg_taille, orient = 'horizontal', length = 200, tickinterval = 5)        
        scale.pack()
        fenetre2.mainloop()
        
def explication():
        showinfo("Explication","""\
Vous disposez d'une grille contenant des mines cachées. En
cliquant sur une case vous connaissez le nombre de mines se
trouvant dans les cases ( 8 au maximum) qui l'entourent. Le
but du jeu est de détecter toutes les mines sans cliquer
dessus. (vous pouvez faire un clic droit de la souris sur
les mines sans qu'elles n'explosent)
                 """)
def chg_niveau(var):
        global niveau
        niveau = var
        game()

def partiedef():
        global taille, niveau
        taille = 10
        niveau = 4
        game()
        
menubar = Menu(fenetre)


menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle Partie", command=game)
#menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Partie", menu=menu1)


menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Changer Taille", command=scaletime)
sub2 = Menu(menu2, tearoff=0)
sub2.add_command(label='50%', command=lambda: chg_niveau(1))
sub2.add_command(label='33%', command=lambda: chg_niveau(2))
sub2.add_command(label='20%', command=lambda: chg_niveau(4))
sub2.add_command(label='15%', command=lambda: chg_niveau(6))
sub2.add_command(label='10%', command=lambda: chg_niveau(9))

menu2.add_cascade(label="Changer Poucentage Mines", menu=sub2)
menu2.add_separator()
menu2.add_command(label="Reglages par defauts", command=lambda : partiedef())
menubar.add_cascade(label="Editer", menu=menu2)


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=explication)
menubar.add_cascade(label="Aide", menu=menu3)


fenetre.config(menu=menubar)

game()

fenetre.mainloop()

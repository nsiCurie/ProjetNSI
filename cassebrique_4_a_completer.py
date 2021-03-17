from tkinter import *

#variable du jeu
largeurEcran=600
hauteurEcran=400
#choix du mur : 4 lignes de 18 briques d'une hauteur de 100px espacées de 10 px
nbBrique=18
nbLigne=4
hauteurMur=100
espaceLigne=10

#programme principal    
 # création de l'objet  Tk
fenetre=Tk()
fenetre.title("Casse-Briques")

 # création d'un canevas dans la fenêtre
can=Canvas(fenetre,height=hauteurEcran,width=largeurEcran)
 # affichage du canevas
can.pack()


def brique(posX,posY,larg,haut,couleur):
     '''fonction qui dessine une brique
    paramètres passés
    posX,posY : position du haut à gauche de la brique
    larg : largeur de la brique
    haut : hauteur d'une brique
    valeur renvoyée : aucune    
    '''
     global can
     can.create_rectangle(posX,posY,posX+larg,posY+haut,fill=couleur,width='1',outline='grey')  

def ligne(posX,posY,nombreBrique,haut):
    '''fonction qui crée une ligne de brique dont la position de la ligne
    paramètres passés
        posX,posY : position du haut à gauche de la ligne
        nombreBrique : un nombre de Brique sur la ligne
        haut: hauteur d'une brique
    valeur renvoyée:
        le tableau représentant la ligne
    '''
    largBrique=largeurEcran/nombreBrique
    #on crée une ligne vide
    laligne=[ ]
    for i in range(nombreBrique):
         brique(posX+i*largBrique,posY,largBrique,haut,'red')
         # on ajoute la brique à la ligne valeur 1 car présente au départ
        '''à compléter : ajouter au tableau ligne ce qui convient ci-dessous , une ligne suffit'''
     #on retourne la ligne créé   sous forme d'un tableau [1,1,1...1] autant de 1 qu'il y a de brique sur la ligne 
    return laligne
        
def mur(nbBrique,nbLigne,hauteurMur,espaceLigne):
     '''fonction qui crée un mur de briques
     paramètres passés
        nbBrique : un nombre de Brique sur la ligne
        nbLigne : nombre de ligne
        hauteurMur : hauteur totale du mur
        espaceLigne : espace entre les lignes
    valeur renvoyée:
        le tableau représentant le mur qui est un tableau de ligne
    '''
     hautBrique = (hauteurMur - (nbLigne -1)*espaceLigne) /nbLigne
     #on crée un mur vide
     lemur=[]
     for i in range(nbLigne):
            #on ajoute la ligne créée au mur
           posX = 0
           posY = (espaceLigne+hautBrique)*(i+1)
          #  il suffit d'appeler la fonction qui fabrique une ligne avec les bons paramètre dans le append
           lemur.append('''à compléter''')
          #on retourne le mur fabriqué    
     return lemur

def  gauche(event):
    '''fonction qui permet de déplacer la raquette avec la flèche gauche'''
    global raqx
    if raqx>dx:
        raqx = raqx -dx
        can.move(raq, -dx, 0)

def  droite(event):
    '''fonction qui permet de déplacer la raquette avec la flèche droite'''
    global raqx
    if  raqx+largraq<largeurEcran:
        raqx = raqx +dx
        can.move(raq, dx,0)

def position_mur(balx,baly):
    '''fonction qui calculer le numéro de la ligne et le numéro de la colonne
     paramètres passés
           balx et baly : coordonnées de la balle
     valeur renvoyée      
        colonne,ligne de la brique touchée
    '''
    hautBrique = (hauteurMur - (nbLigne -1)*espaceLigne) /nbLigne
    # il suffit de calculer le quotient de la position de la balle par la hauteur d'une rangée  qui vaut (espaceLigne+hauteurBrique)
    #attention comme un tableau commence à 0 et que ce calcul donnera dans le plus petit cas 1 (1ère ligne ), il faut retirer 1
    ligne = '''à compléter'''
    # la position de la brique s'obtient en calculant le quotient de la largeur de l'écran par largeurBrique
    largeurBrique=largeurEcran/nbBrique  
    colonne ='''à compléter'''
    return int(colonne),int( ligne)

def bouge_balle():
    '''fonction qui déplace la balle et fait les test de collision'''
    global balx,baly,dbx,dby,raqx
    #position du mur touché
    colonne, ligne = position_mur(balx,baly)
    #il faut vérifier que la ligne trouvée est inférieure au nombre de ligne du mur
    # et que la brique touchée n'est pas déjà détruire donc ==1 ou !=0
    #on accède à la brique en récupérant lemur[ligne][colonne]
    if  '''à compléter''':
                #les briques sont numérotés de 1 à nbBrique* nbLigne, ligne par ligne
                #quel est l'index de la brique située à la ligne "ligne" et la colonne "colonne" sachant qu'un mur à nbBrique par ligne
                index='''à compléter'''
                #on efface la brique dessinée  de l'index correspondant 
                can.delete (index)
                #on met à jour sa représentation en mémoire 1 pour visible 0 pour détruite dans le tableau lemur
                '''à compléter'''
                # la balle a touché le mur, elle rebondit 
                dby=-dby
    #touche l'écran à droite            
    if  balx+dbx>largeurEcran:
        dbx=-dbx
    # touche l'écran à gauche    
    if  balx+dbx<0:
        dbx=-dbx
    #descend en dessous de la raquette    
    if  baly>raqy:
        #on l'a fait rebondir car ici la raquette va suivre la balle
        dby=-dby
    #touche le haut de l'écran    
    if  baly+dby<0:
        #elle rebondit
        dby=-dby
    #on bouge la balle du déplacement qui convient    
    balx=balx+dbx
    baly=baly+dby
    can.move(balle,dbx,dby)
    #on calcule les coordonnées de la raquette pour qu'elle reste sous la balle
    draqx=balx-raqx-largraq/2
    raqx=balx-largraq/2
    # et on la bouge (mode démo)
    can.move(raq, draqx,0)
    #cette partie sera à retravailler en mode jeu
    fenetre.after(10,bouge_balle) 




#création du mur
lemur = mur(nbBrique,nbLigne,hauteurMur,espaceLigne)
#affichage de la représentation mémoire du mur
print(lemur)
#création de la raquette
largraq=40
raqx=largeurEcran/2-largraq
raqy=hauteurEcran-30
raq=can.create_rectangle(raqx,raqy,raqx+largraq,raqy+10,fill='white')
#nombre de pixel pour le déplacement de la raquette
dx=5
# on positionne la balle au centre de la raquette
balx=raqx+largraq/2
baly=raqy-5
#nombre de pixel pour le déplacement de la balle
dbx=5 #la balle va vers la droite dbx>0
dby=-5 #la balle remontera car dby<0
#creation de la balle
balle=can.create_oval(balx-5,baly-5,balx+5,baly+5,fill='yellow')
#on met en marche la balle
bouge_balle()

 # on ajoute l'écouteur d'événement
fenetre.bind('<Left>', gauche)
fenetre.bind('<Right>', droite)   
# boucle principale
fenetre.mainloop()

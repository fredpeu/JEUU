import pygame
import random as rdm
from utils import *
import time


pygame.init()

# initialisation de l´écran avec sa taille et le titre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()

# dessiner un rectangle:
        # Créer un rectangle: rectangle= pygame.Rect(x,y,largeur,hauteur)
        # Le dessiner:        pygame.draw.rect(screen,couleur,rectangle)
        
# dessiner un cercle: pygame.draw.circle(screen,couleur, [x, y], rayon)

# ajouter du texte:
    #font1 = pygame.font.SysFont(None, 72)
    #txt1 = font1.render('NSI FOR EVER', True, GREY)

# ajouter une image:
    # vaisseau=pygame.image.load('vaisseau.png')
    # rect_vaisseau=vaisseau.get_rect()

# Dessiner texte ou image dans la boucle du jeu:
    # texte: screen.blit(txt1,(x,y))
    # image: screen.blit(vaisseau,rect_vaisseau)

vaisseau=pygame.image.load('vaisseau.png')
rect_vaisseau=vaisseau.get_rect()


        

run = True
# -------- Boucle principale du jeu -----------
while run:
    # fond d´écran
    screen.fill(WHITE)
    # --- Gestion des évènements
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clic souris")
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print("barre espace")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect_vaisseau.top-=3
    if keys[pygame.K_DOWN]:
        rect_vaisseau.top+=3
    if keys[pygame.K_RIGHT]:
        rect_vaisseau.left+=3
    if keys[pygame.K_LEFT]:
        rect_vaisseau.left-=3


    
    # Dessins

    screen.blit(vaisseau,rect_vaisseau)




    # 60 mises à jour par seconde
    clock.tick(60)
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()
 

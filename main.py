import pygame
import random
from Player import *
from Rivales import *
from Balas import *
from LibreriaGeneral import *
#--------------------------------------------
width = 1080
high = 720
#---------------------------------------------
if __name__ == "__main__":
    #DefinicionVariables
    pygame.init()
    end = False
    reloj = pygame.time.Clock()
    points = 50
    window = pygame.display.set_mode([width,high])
    Player1 = Jugador()
    PlayersList = pygame.sprite.Group()
    PlayersList.add(Player1)
    Rivals = pygame.sprite.Group()
    Balas = pygame.sprite.Group()
    QuantityRivals = 20
    for i in range(QuantityRivals):
        x = 1000
        y = random.randrange(high)
        vx = -1*random.randrange(15)
        vy = 0
        r = Rival([x,y],vx,vy)
        Rivals.add(r)
        
    while not end:
        #Gestion Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = Player1.ReturnPosition()
                    bullet = PlayerBullets(position)
                    Balas.add(bullet)
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                PlayersList.update(position)
        #Control
        #Limpieza
        for b in Balas:
            if b.rect.x > (width + b.rect.w):
                Balas.remove(b)
            if b.getDistance() == 50:
                Balas.remove(b)
        #Colision
        ls_col = pygame.sprite.spritecollide(Player1, Rivals, False)
        for r in ls_col:
            points -= 1
        #Refrescar
        print points
        Rivals.update()
        Balas.update()
        window.fill([0,0,0])
        Rivals.draw(window)
        Balas.draw(window)
        PlayersList.draw(window)
        pygame.display.flip()
        reloj.tick(60)

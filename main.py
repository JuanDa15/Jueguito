import pygame
import random
from Player import *
from Rivales import *
from Life import *
from Balas import *
from LibreriaGeneral import *
#--------------------------------------------
width = 1080
high = 720
pygame.init()
window = pygame.display.set_mode([width,high])
#---------------------------------------------
if __name__ == "__main__":
    #seccion antes del juego
    music = pygame.mixer.Sound('Intergalactic Odyssey.ogg')
    FuentePre = pygame.font.Font(None, 40)
    Tittle = FuentePre.render('Cosita',True,SelectColor('White'))
    music.play(-1)
    end = False
    endPrev = False
    while (not end) and (not endPrev):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                endPrev = True
        window.blit(Tittle,[500,250])
        pygame.display.flip()
    music.stop()
    #seccion del juego
    #DefinicionVariables
    BulletSound = pygame.mixer.Sound('laser8.wav')
    fuentej = pygame.font.Font(None, 32)
    #end = False
    EndGame = False
    reloj = pygame.time.Clock()
    Player1 = Jugador()
    PlayersList = pygame.sprite.Group()
    PlayersList.add(Player1)
    Rivals = pygame.sprite.Group()
    Balas = pygame.sprite.Group()
    BalasEnemigas = pygame.sprite.Group()
    QuantityRivals = 2
    for i in range(QuantityRivals):
        x = 1000
        y = random.randrange(high)
        vx = -1*random.randrange(1,10)
        vy = 0
        r = Rival([x,y],vx,vy)
        Rivals.add(r)
        
    while not end and not EndGame:
        #Gestion Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = Player1.ReturnPosition()
                    bullet = PlayerBullets(position)
                    Balas.add(bullet)
                    BulletSound.play()
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                PlayersList.update(position)
        #Control
        #Control Rivales
        for r in Rivals:
            if r.timer < 0:
                position = r.ReturnPosition()
                bullet = RivalBullets(position)
                BalasEnemigas.add(bullet)
                r.timer = 60
        #Limpieza
        for b in Balas:
            #BulletsCollision = pygame.sprite.spritecollide(b, Rivals, True)
            if b.rect.x > (width + b.rect.w):
                Balas.remove(b)
            if b.getDistance() == 35:
                Balas.remove(b)
        for b in BalasEnemigas:
            #BulletsCollision = pygame.sprite.spritecollide(b, Rivals, True)
            #for r in BulletsCollision:
            #    Balas.remove(b)
            if b.rect.x < (0 + b.rect.w):
                BalasEnemigas.remove(b)
            if b.getDistance() == 75:
                BalasEnemigas.remove(b)
        BulletRivalsColl = pygame.sprite.groupcollide(Balas, Rivals, True, True)
        BulletRivalsColl = pygame.sprite.groupcollide(BalasEnemigas, PlayersList, True, False)
        for players in BulletRivalsColl:
            if players in BulletRivalsColl:
                Player1.life -= 1
        
        for player in PlayersList:
            if player.life <= 0:
                EndGame = True
        #Colision
        PlayerCollision = pygame.sprite.spritecollide(Player1, Rivals, True)
        #Refrescar
        Rivals.update()
        BalasEnemigas.update()
        Balas.update()
        window.fill([0,0,0])
        if Player1.life == 3:
            LifeImage = pygame.image.load('3Hearts.png')
            window.blit(LifeImage,[10,10])
        elif Player1.life == 2:
            LifeImage = pygame.image.load('2Hearts.png')
            window.blit(LifeImage,[10,10])
        elif Player1.life == 1:
            LifeImage = pygame.image.load('Hearts.png')
            window.blit(LifeImage,[10,10])
        Rivals.draw(window)
        Balas.draw(window)
        BalasEnemigas.draw(window)
        PlayersList.draw(window)
        pygame.display.flip()
        reloj.tick(60)
    
    #despues de juego       
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        fuente = pygame.font.Font(None, 34)
        EndTittle = fuente.render('Fin de Juego', True, SelectColor('White'))
        window.fill(SelectColor('Black'))
        window.blit(EndTittle,[width/2,high/2])
        pygame.display.flip()
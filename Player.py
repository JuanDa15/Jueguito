import pygame
width = 1080
high  =720

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pelota Jugador.png')
        self.rect = self.image.get_rect()
        position = [50,360]
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.life = 3
        
    def update(self,pos):
        self.rect.x = pos[0] - 32
        #self.rect.x+=self.velx
        if self.rect.x > width:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 1080
        self.rect.y = pos[1] - 32
        #self.rect.y+=self.vely
        if self.rect.y > high:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = 720
    
    def ReturnPosition(self):
        Xpos = self.rect.x + 32
        Ypos = self.rect.y + 15
        return [Xpos,Ypos]
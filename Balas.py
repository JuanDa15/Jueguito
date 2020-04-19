import pygame

class bullets(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velocityX = 0
        
    def update(self):
        pass
    

class PlayerBullets(bullets):
    def __init__(self,pos):
        bullets.__init__(self)
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bala Jugador.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.distance = 0
        self.velocityX = 12
        
    def update(self):
        self.rect.x += self.velocityX
        self.distance += 1

    def getDistance(self):
        return self.distance

class RivalBullets(bullets):
    def __init__(self,pos):
        bullets.__init__(self)
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bala Rival.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.distance = 0
        self.velocityX = -12
        
    def update(self):
        self.rect.x += self.velocityX
        self.distance += 1

    def getDistance(self):
        return self.distance
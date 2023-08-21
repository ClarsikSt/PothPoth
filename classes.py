import pygame
class Coins(pygame.sprite.Sprite):
    def __init__(self,naminal,size,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.naminal = naminal
        self.image = pygame.transform.scale(pygame.image.load('coin.png'),size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.namonal += 1
    def reset(self,mw):
        mw.blit(self.image,(self.rect.x,self.rect.y))
class Block(pygame.sprite.Sprite):
    def __init__(self,image,size,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image),size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self,mw):
        mw.blit(self.image,(self.rect.x,self.rect.y))
class Slot(pygame.sprite.Sprite):
    def __init__(self,size,x,y,typer = None,intem = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('slot.png'),size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.intem = intem
        self.type = typer
    def reset(self,mw):
        mw.blit(self.image,(self.rect.x,self.rect.y))
        if self.intem != None:
            mw.blit(self.intem,(self.rect.x,self.rect.y))
    def add(self, intem, typer = None):
        self.intem = intem
        self.type = typer

class Hero(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('hero.png'),size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self,mw):
        mw.blit(self.image,(self.rect.x,self.rect.y))
class Ore(pygame.sprite.Sprite):
    def __init__(self,image,size,x,y,cash,icon,power):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image),size)
        self.icon = pygame.transform.scale(pygame.image.load(icon),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cash = cash
        self.power = power
    def reset(self,mw):
        mw.blit(self.image,(self.rect.x,self.rect.y)) 
class Intem(pygame.sprite.Sprite):
    def __init__(self,image,size,x,y,types):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image),size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = types
        
    def reset(self,mw):
        mw.blit(self.image,(self.rect.x,self.rect.y)) 
class SlotsAmmo():
    def __init__(self,x,y,ammo,fonty):
        self.image = fonty.render('x '+str(ammo),True,(255,255,255))
        self.x = x
        self.y = y
        self.nomber = ammo
        
    def reset(self,mw):
        mw.blit(self.image,(self.x,self.y)) 
    def update(self,fonty):
        self.image = fonty.render('x '+str(self.nomber),True,(255,255,255))



        


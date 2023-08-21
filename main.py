import pygame
import classes
from random import randint
coin = classes.Coins(10,(35,50),100,100)
pygame.font.init()
#brick = classes.Block('brick.png',(50,50),0,0)

sfont = pygame.font.SysFont('arial', 15)

slot1 = classes.Slot((50,50),0,0)
slot2 = classes.Slot((50,50),51,0)
slot3 = classes.Slot((50,50),102,0)
slot4 = classes.Slot((50,50),153,0)
slot5 = classes.Slot((50,50),204,0)
slot6 = classes.Slot((50,50),255,0)
slot7 = classes.Slot((50,50),306,0)
slot8 = classes.Slot((50,50),357,0)
slot9 = classes.Slot((50,50),408,0)
slot10 = classes.Slot((50,50),459,0)
slots = [slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9,slot10]
nombers = list()
x = 22
for i in range(10):
    t = classes.SlotsAmmo(x,35,0, sfont)
    nombers.append(t)
    x += 51


h = classes.Hero((50,50),0,50)

cfont = pygame.font.SysFont('comicsans', 50)
coins = 0

ground = (100,200,100)

HEIGHT = 500
WEIGHT = 700

mw = pygame.display.set_mode((WEIGHT, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('miniG')
mw.fill(ground)
  
pygame.display.flip()
  
running = True

places = list()
x = 0
y = 50

drop = pygame.sprite.Group()
drop2 = list()

coppers = pygame.sprite.Group()
stones = pygame.sprite.Group()
irons = pygame.sprite.Group()
golds = pygame.sprite.Group()
trees = pygame.sprite.Group()

bricks = pygame.sprite.Group()

b = classes.Block('grass.png',(50,50),x,y)
bricks.add(b)
for i in range(125):
    x += 50
    if x >= WEIGHT:
        x = 0
        y += 50
    change = randint(1,100)
    if change <= 25:
        t = classes.Ore('tree.png',(50,50),x,y,randint(1,5),'woodicon.png',3)
        trees.add(t)
    elif change < 28:
        g = classes.Ore('gold.png',(50,50),x,y,randint(100,200),'goldicon.png',25)
        golds.add(g)
    elif change < 36:
        g = classes.Ore('iron.png',(50,50),x,y,randint(50,100),'ironicon.png', 15)
        irons.add(g)
    elif change < 45:
        g = classes.Ore('copper.png',(50,50),x,y,randint(25,50),'coppericon.png', 10)
        coppers.add(g)
    elif change < 60:
        g = classes.Ore('stone.png',(50,50),x,y,randint(5,25),'stoneicon.png', 5)
        stones.add(g)
    minilist = [x,y]
    places.append(minilist)
    b = classes.Block('grass.png',(50,50),x,y)
    bricks.add(b)

def go_to_slot(who,typeofwho):
    global slots, nombers
    i = 0
    for slot in slots:
        if slot.type == None or slot.type == typeofwho and nombers[i].nomber < 32:
            nombers[i].nomber += 1
            slot.add(pygame.image.load(typeofwho+'icon.png'),typeofwho)
            break
        i+=1





while running:
    mw.fill(ground)

    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            
                
            if event.key == pygame.K_RIGHT and h.rect.x <= WEIGHT - 51:
                h.rect.x += 50
            elif event.key == pygame.K_LEFT and h.rect.x >= 50:
                    h.rect.x -= 50
            elif event.key == pygame.K_UP and h.rect.y >= 100:
                h.rect.y -= 50
            elif event.key == pygame.K_DOWN and h.rect.y <= HEIGHT - 51:
                h.rect.y += 50
            hits = pygame.sprite.spritecollide(h, trees, True)
            hits1 = pygame.sprite.spritecollide(h, stones, True)
            hits2 = pygame.sprite.spritecollide(h, golds, True)
            hits3 = pygame.sprite.spritecollide(h, coppers, True)
            hits4 = pygame.sprite.spritecollide(h, irons, True)
            if hits or hits1 or hits2 or hits3 or hits4:
                for hit in hits:
                    for i in range(randint(1,2)):
                        droping = classes.Intem('woodicon.png',(25,25),hit.rect.x+ randint(-5,25),hit.rect.y+ randint(-5,25),'wood')
                        drop.add(droping)
                for hit in hits1:
                    droping = classes.Intem('stoneicon.png',(25,25),hit.rect.x+ randint(-5,25),hit.rect.y+ randint(-5,25),'stone')
                    drop.add(droping)
                for hit in hits2:
                    droping = classes.Intem('goldicon.png',(25,25),hit.rect.x+ randint(-5,25),hit.rect.y+ randint(-5,25),'gold')
                    drop.add(droping)
                for hit in hits3:
                    droping = classes.Intem('coppericon.png',(25,25),hit.rect.x+ randint(-5,25),hit.rect.y+ randint(-5,25),'copper')
                    drop.add(droping)
                for hit in hits4:
                    droping = classes.Intem('ironicon.png',(25,25),hit.rect.x+ randint(-5,25),hit.rect.y+ randint(-5,25),'iron')
                    drop.add(droping)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            for c in drop:
                if c.rect.collidepoint(x,y): 
                    
                    go_to_slot(c,c.type)
                    c.kill()

            

    #coin.reset(mw)
    #brick.reset(mw)
    ct = cfont.render(str(coins)+'$',True,(220,220,0))
    slot1.reset(mw)
    slot2.reset(mw)
    slot3.reset(mw)
    slot4.reset(mw)
    slot5.reset(mw)
    slot6.reset(mw)
    slot7.reset(mw)
    slot8.reset(mw)
    slot9.reset(mw)
    slot10.reset(mw)
    for s in nombers:
        s.update(sfont)
        s.reset(mw)
    
    bricks.draw(mw)#Все отображение после групп
    trees.draw(mw)
    coppers.draw(mw)
    stones.draw(mw)
    irons.draw(mw)
    golds.draw(mw)
    drop.draw(mw)
    mw.blit(ct,(520,7))
    clock.tick(120)
    h.reset(mw)
    pygame.display.update()
    pygame.display.flip()
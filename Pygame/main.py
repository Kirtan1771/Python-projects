from msvcrt import setmode
import pygame as pg
import random
import math

pg.init()   # Initialize pygame

# Create the screen size

screen = pg.display.set_mode((800,600))   # Height = 600 width = 800

# Icon and Title for our game
pg.display.set_caption("SpaceJam")   
icon = pg.image.load('ufo.png')  
pg.display.set_icon(icon) 

# Background
background = pg.image.load('background2.jpg')      


# Player
playerImg = pg.image.load('hero1.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pg.image.load('enemy1.png')
enemyX = random.randint(0,736)
enemyY = random.randint(0,400)
enemyX_change = 0.2
enemyY_change = 40

# Bullet
bulletImg = pg.image.load('laser.png')
bulletX = 0
bulletY = 486
bulletX_change = 0
bulletY_change = 3
bullet_state = 'ready'

score = 0
font = pg.font.Font('vhs-gothic.ttf', 32)
textX = 20
textY = 20


def show_score(x, y):
    score_text = font.render("SCORE: " + str(score), True, (255,255,255))
    screen.blit(score_text, (x, y))
#Drawing image on the screen using blit()
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16 , y+10))

def ifCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:  
        return True
    else:
        return False
    
# Breaking the loop so that the screen does not vanish.
running = True
while running:
    screen.fill((0,0,0))
    
    # Adding backgroud image
    screen.blit(background, (0,0))
    
    # Player movement
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    # Update the screen
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    # if keystroke is pressed check whether its right or left
    # Keydown is pressing a key down & Keyup is releasing a key
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -0.5
            if event.key == pg.K_RIGHT:
                playerX_change = 0.5
        
            if event.key == pg.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY) 
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0
          
            
                

    playerX += playerX_change
    playerY += playerY_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    
    enemyX += enemyX_change    
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change
        
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 486
        bullet_state ='ready'
    
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    collision = ifCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 486
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(0,736)
        enemyY = random.randint(0,400)
        
    
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pg.display.update()
    
    
         
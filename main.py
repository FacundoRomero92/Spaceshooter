import pygame
import random
import math
# inicializar pygame
pygame.init()
# set window
screen= pygame.display.set_mode((800,600))
pygame.display.set_caption('kodland')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

black=(0,0,0)
white=(255,255,255)
#jugador

playership= pygame.image.load('player.png')

playerX=368
playerY=600

playerX_change=0
playerY_change=0 

def player(x,y):
    screen.blit(playership,(x,y))

#score
score_value=0
fonttitle=pygame.font.Font('freesansbold.ttf', 64)
font=pygame.font.Font('freesansbold.ttf', 32)
textx=10
texty=10
def showscore(x,y,color):
    score = font.render("Score: "+str(score_value),True, color)
    screen.blit(score, (x,y))

#menu

menu=True
texto1= "LLUVIA DE METEOROS"
texto2="Presiona ENTER para jugar"
texto3="Presiona ESCAPE para salir"
textovacio=""
posx=40
posy=220
t2x=posx+150
t2y=posy+90
t3x=posx+150
t3y=posy+130
def showsmenu(font,texto,color,posx,posy):
    letramenu = font.render(texto,True, color)
    screen.blit(letramenu, (posx,posy))
#gameovertext

gameover="GAME OVER"
gameover2="presiona enter para volver a jugar"
gameover3="presiona ESCAPE para salir"
posgameover= 205
#enemigos
meteoro=pygame.image.load('luna.png')

enemyX=random.randint(0,564)
enemyY=0

enemyY_change=0

def enemy(x,y):
    screen.blit(meteoro,(x,y))
#Bala
bala=pygame.image.load('bala.png')
balax=0
balay=1000
bulletState="ready"
balaY_change=-0.4

def disparo(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bala,(x+26,y-10))

key = pygame.key.get_pressed()

#colision
def colisiona(enemyX,enemyY,balax,balay):
    distance = math.sqrt((math.pow((enemyX-15) - balax, 2))+(math.pow(enemyY -balay ,2)))
    if distance<=27:
        return True

# correr el juego
running=True
while running:
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change= 0.2
            if event.key == pygame.K_LEFT:
                playerX_change= -0.2
            if event.key == pygame.K_UP:
                playerY_change= -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
            if event.key == pygame.K_SPACE:
                if bulletState=="ready":    
                    balax=playerX
                    balay=playerY
                    disparo(balax,balay)
                    
            if event.key == pygame.K_RETURN:
                if menu==True: 
                    black=white
                    enemyY=0
                    enemyY_change=0.1
                    texto1=textovacio
                    texto2=textovacio
                    texto3=textovacio
                    menu=False
            if event.key ==pygame.K_ESCAPE:
                running=False
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
    screen.fill((black))
#enemigos 
    enemy(enemyX,enemyY)
    enemyY+=enemyY_change
#colisiones
    colision=colisiona(enemyX,enemyY,balax,balay)
    if colision:
        score_value+=1
        bulletState="ready"
        enemyX=random.randint(0,764)
        enemyY=0
#Jugador
    if balay<=0:
       bulletState="ready"
        
    if bulletState == "fire":
        disparo(balax,balay)
        balay+=balaY_change

    if event.type== pygame.KEYUP:
        playerX_change=0
        playerY_change=0

    playerX+=playerX_change
    playerY+=playerY_change

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    if playerY<=0:
        playerY=0
    elif playerY>=536:
        playerY=536
#Game Over
    if enemyY>=600:
        texto1=gameover
        texto2=gameover2
        texto3=gameover3
        black=(0,0,0)
        playerX=368
        playerY=600
        posx=posgameover
        t2x=posx-75
        t3x=t2x+50  
        menu=True

    showsmenu(fonttitle,texto1,white,posx,posy)
    showsmenu(font,texto2,white,(t2x),(t2y) )
    showsmenu(font,texto3,white,(t3x),(t3y))
    showscore(textx,texty,(0,0,0))
    player(playerX,playerY)
    pygame.display.update()


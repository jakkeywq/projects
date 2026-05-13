import pygame
import time

import menu
import thorns

pygame.init()

screenWidth = 400
screenHeight = 600

white = (255, 242, 242)
blue = (0, 0, 255)
red = (216, 64, 64)

grey = (104, 87, 82)
lighterGrey = (153, 124, 112)

decoColor = (28, 28, 28)


icon = pygame.image.load('sprites/icon.png')
screen = pygame.display.set_icon(icon)
screen = pygame.display.set_caption('chicken trip')

screen = pygame.display.set_mode((screenWidth, screenHeight))

gravity = 0.2
jumpPower = -5
playerSpeed = 4

direction = True # default direction - right
score = 0

class Player():
    def __init__(self):
        self.rect = pygame.Rect(200, 200, 50, 50)
        self.velY = jumpPower

        self.sprite = pygame.image.load('sprites/player.png')
        self.sprite = pygame.transform.smoothscale(self.sprite, (self.rect.width+5, self.rect.height+5))

        self.hitbox = self.sprite.get_rect()
        self.hitbox.center = self.rect.center


    def moving(self):
        if direction:
            self.rect.x += playerSpeed
        if not direction:
            self.rect.x -= playerSpeed

    def jump(self):

        self.velY = jumpPower
        return

    def gravity(self):

        self.velY += gravity
        self.rect.y += self.velY

    def collision(self):

        global run

        global direction
        global score

        global leftBorders
        global rightBorders

    
        for each in platformList:
            if self.rect.colliderect(each):


                if self.velY < 0:
                    self.velY = jumpPower*0.5 # maybe i'll change that


                if direction:
                    rightBorders = []
                    leftBorders = thorns.drawLeftThorn()
                else:
                    rightBorders = thorns.drawRightThorn()
                    leftBorders = []

                direction = not direction
                score += 1
                

        for each in borderList:
            if self.rect.colliderect(each):
                self.rect.x, self.rect.y = 175, 200
                self.velY = jumpPower

                leftBorders = []
                rightBorders = []
                drawAll()
                
                
                if menu.openMenu(score):
                    score = 0 
                    direction = True

                else:
                    run = False

            
        for each in [*leftBorders, *rightBorders]:
            if self.rect.colliderect(each):
 
                self.rect.x, self.rect.y = 175, 200
                self.velY = jumpPower

                leftBorders = []
                rightBorders = []
                drawAll()
                
                
                if menu.openMenu(score):
                    score = 0 
                    direction = True

                else:
                    run = False

                
    def draw(self):
        self.hitbox.center = self.rect.center
        screen.blit(self.sprite, self.hitbox)

        #pygame.draw.rect(screen, blue, self.rect)
        

decoList = [
    pygame.Rect(0, 0, 7, 600),
    pygame.Rect(393, 0, 7, 600),
    pygame.Rect(0, 593, 400, 7),
    pygame.Rect(0, 0, 400, 7)
]

platformList = [
    pygame.Rect(0, 0, 20, 600),
    pygame.Rect(380, 0, 20, 600)
]

borderList = [
    pygame.Rect(20, 580, 360, 20),
    pygame.Rect(20, 0, 360, 20)
]

leftBorders = []

rightBorders = []

colliderList = [platformList, borderList, leftBorders, rightBorders]

run = True
clock = pygame.time.Clock()

player = Player()


def drawAll():

    global borderImage

    drawList = platformList + borderList + leftBorders + rightBorders + decoList

    for each in drawList:
        if each in platformList:
            color = grey
        if each in borderList:
            color = lighterGrey
        if each in leftBorders or each in rightBorders:
            color = red # i should change it soon
        if each in decoList:
            color = decoColor


        pygame.draw.rect(screen, color, each)

    player.draw()

    pygame.display.update()




while run:

    screen.fill(white)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and pygame.K_SPACE:
            player.jump()

    player.moving()
    player.gravity()
    player.collision()

    drawAll()

    clock.tick(60)
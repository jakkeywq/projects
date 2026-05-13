import pygame
import os

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('AIZEN TRIP')


bgColor = (239, 239, 239)
endColor = (255, 167, 37)

platformColor = (63, 125, 88)
floorColor = (239, 150, 81)
spikeColor = (236, 82, 40)


gravity = 0.5
jumpPower = -7
playerSpeed = 5


class Player:


    def __init__(self):

        self.rect = pygame.Rect(100, 450, 50, 50)
        
        self.velY = 0
        self.onGround = False

        self.isJumping = False
        self.jumpTime = 0

        self.image = pygame.image.load('sprites/aizen.png')
        self.image = pygame.transform.smoothscale(self.image, (self.rect.width, self.rect.height))


    def move(self, keys):

        if keys[pygame.K_LEFT]:
            self.rect.x -= playerSpeed
        if keys[pygame.K_RIGHT]:
            self.rect.x += playerSpeed

        if keys[pygame.K_SPACE] and self.onGround:
            self.velY = jumpPower
            self.onGround = False

            self.isJumping = True

        if keys[pygame.K_SPACE] and self.isJumping:
            self.jumpTime += 0.1
            self.velY = jumpPower - (self.jumpTime * 0.5)
            if self.jumpTime > 1:
                self.isJumping = False
                self.jumpTime = 0
                pass

        if not keys[pygame.K_SPACE]:
            self.isJumping = False
            self.jumpTime = 0


    def applyGravity(self, platforms):
        self.velY += gravity
        self.rect.y += self.velY



        for each in platforms:
            if self.rect.colliderect(each) and self.velY > 0:

                self.rect.bottom = each.top
                self.velY = 0
                self.onGround = True
                break
        else:
            self.onGround = False

        for each in spikes:
            if self.rect.colliderect(each):

                self.rect.x = 100
                self.rect.y = 420

        
    def draw(self):
        screen.blit(self.image, self.rect)


platforms = [

    pygame.Rect(75, 475, 100, 20), #spawn

    pygame.Rect(75, 350, 100, 20),

    pygame.Rect(300, 425, 50, 20),
    pygame.Rect(600, 425, 50, 20),

    pygame.Rect(700, 300, 50, 20),

    pygame.Rect(600, 175, 20, 20),
    pygame.Rect(320, 175, 200, 20),

    pygame.Rect(100, 100, 50, 20)


]

spikes = [

    pygame.Rect(0, 530, 800, 20), # floor

    pygame.Rect(75, 370, 100, 20),
    pygame.Rect(200, 250, 20, 300),

    pygame.Rect(300, 250, 350, 20),
    pygame.Rect(450, 375, 20, 175),

    pygame.Rect(550, 70, 20, 200),
    pygame.Rect(375, 0, 100, 50),
    pygame.Rect(400, 155, 50, 20),

    pygame.Rect(200, 75, 20, 75)

]

prize = [
    pygame.Rect(110, 50, 30, 30)
]

player = Player()


run = True
clock = pygame.time.Clock()

while run:
    screen.fill(bgColor)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.move(keys)
    player.applyGravity(platforms)
    player.draw()


    floor = pygame.Rect(0, 550, screenWidth, 50)
    pygame.draw.rect(screen, floorColor, floor)



    for each in platforms:
        pygame.draw.rect(screen, platformColor, each)

    for each in spikes:
        pygame.draw.rect(screen, spikeColor, each)

    for each in prize:
        pygame.draw.rect(screen, endColor, each)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
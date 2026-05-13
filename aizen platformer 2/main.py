import pygame

import data

pygame.init()

screen = pygame.display.set_mode((800, 600))




class Player:
    def __init__(self):

        self.rect = pygame.Rect(75, 400, 50, 50)
        self.drop = 0
        self.ground = False

        self.hop = False
        self.hopTime = 0

        self.direction = True
        self.moving = True

        self.image = pygame.image.load('sprites/player.png')
        self.image = pygame.transform.smoothscale(self.image, (self.rect.width, self.rect.height))


    def move(self, keys):

        if keys[pygame.K_RIGHT]:

            self.rect.x += data.speed

            self.direction = True
            self.moving = True

        if keys[pygame.K_LEFT]:

            self.rect.x -= data.speed

            self.direction = False
            self.moving = True

        if not keys[pygame.K_RIGHT] and not [pygame.K_LEFT]:

            self.moving = False



        if keys[pygame.K_SPACE] and self.ground == True:

            self.drop = data.hopPower
            self.ground = False

            self.hop = True

        if keys[pygame.K_SPACE] and self.hop:

            self.hopTime += 0.1

            if self.hopTime > 0.5:
                self.drop = data.hopPower - (self.hopTime*0.25) 

            if self.hopTime > 1:

                self.hop = False
                self.hopTime = 0
                pass
            
        if not keys[pygame.K_SPACE]:

            self.hop = False
            self.hopTime = 0

    def collide(self, keys):

        self.drop += data.gravity
        self.rect.y += self.drop


        for each in data.platforms[data.levelID]:

            if self.rect.colliderect(each) and self.drop > 0:

                self.rect.bottom = each.top
                self.ground = True

                self.drop = 0

                break

            else:
                
                self.ground = False

        for each in data.obstacles[data.levelID]:

            if self.rect.colliderect(each):

                self.rect.x = data.startPos[(data.levelID)][0]
                self.rect.y = data.startPos[(data.levelID)][1]

                self.drop = 0


        for each in data.borders:

            if self.rect.colliderect(each) and self.moving:

                if self.direction:
                    self.rect.right = each.left

                if not self.direction:
                    self.rect.left = each.right


        for each in data.passages[data.levelID]:

            if self.rect.colliderect(each):
                if self.drop == 0:
                    if keys[pygame.K_SPACE]:
                        levelPassed(self)
                    


    def draw(self):
        #pygame.draw.rect(screen, blue, self.rect)
        screen.blit(self.image, self.rect)


def levelPassed(self):
    
    data.levelID += 1
    print(data.levelID)

    self.rect.x = data.startPos[(data.levelID)][0]
    self.rect.y = data.startPos[(data.levelID)][1]

    
    self.ground = False

run = True
clock = pygame.time.Clock()

player = Player()

while run:

    screen.fill(data.bgColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for each in data.platforms[data.levelID]:
        pygame.draw.rect(screen, data.platformColor, each)

    for each in data.obstacles[data.levelID]:
        pygame.draw.rect(screen, data.obstacleColor, each)

    for each in data.passages[data.levelID]:
        pygame.draw.rect(screen, data.passageColor, each)


    player.collide(keys)
    player.move(keys)
    player.draw()


    pygame.display.update()
    clock.tick(60)

pygame.quit()
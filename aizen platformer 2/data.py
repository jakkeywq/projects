import pygame

# values

gravity = 0.4
hopPower = -8
speed = 5
levelID = 1

# colors

blue = (0, 0, 255)
platformColor = (128, 128, 128)
obstacleColor = (255, 0, 0)
passageColor = (0, 255, 100)
bgColor = (255, 255 ,255)

# collide lists

borders = [
    pygame.Rect(-60, 0, 10, 600),
    pygame.Rect(860, 0, 10, 600),
]


platforms = {
    1: [
        pygame.Rect(-100, 550, 1000, 50), #floor

        pygame.Rect(155, 530, 20, 20),

        pygame.Rect(200, 400, 100, 20),
        pygame.Rect(450, 450, 100, 20),
        pygame.Rect(625, 275, 100, 20),

        pygame.Rect(100, 150, 300, 40)

    ],

    2: [
        pygame.Rect(-100, 550, 1000, 50), #floor
        
        pygame.Rect(600, 350, 100, 20),
        pygame.Rect(600, 200, 100, 20),

    ]
}


obstacles = {
    1: [
        pygame.Rect(175, 540, 625, 10)
    ],

    2: [
        pygame.Rect(300, 540, 300, 10)
    ]
}


passages = {
    1: [pygame.Rect(150, 70, 60, 80)],
    2: [pygame.Rect(75, 470, 60, 80)]
}

startPos = {
    1: [75, 400],
    2: [675, 400]
}
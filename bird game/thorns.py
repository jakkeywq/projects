import pygame
import random

#left - x=20, 580>y>20

thornSize = 20, 60

patternList = {
    '1': [
        pygame.Rect(0, 55, *thornSize),
        pygame.Rect(0, 185, *thornSize),
        pygame.Rect(0, 500, *thornSize)
    ],

    '2': [
        pygame.Rect(0, 150, *thornSize),
        pygame.Rect(0, 390, *thornSize)
    ],

    '3': [
        pygame.Rect(0, 40, *thornSize),
        pygame.Rect(0, 140, *thornSize),
        pygame.Rect(0, 240, *thornSize)
    ]

}


def drawLeftThorn():

    thorns = random.choice(list(patternList.values()))
    for each in thorns:
        each[0] = 20

    return thorns

def drawRightThorn():
    
    thorns = random.choice(list(patternList.values()))
    for each in thorns:
        each[0] = 360

    return thorns
from sprites import Lander, Landing
from items import Rock1, Rock2, Rock3, Satellite1, Satellite2, Building1, Building2, Building3, Meteors
import pygame, random


class Player:

    def __init__(self):
        self.lives = 3
        self.score = 0
        self.lander, self.zone1,self.zone2,self.zone3 = 0,0,0,0
        self.c1, self.c2, self.c3, self.c4, self.c5, = 0,0,0,0,0
        self.Meteor = 0

    # start the game by init a new lander
    def begin(self, screen):
        self.lander = Lander(screen)
        self.lander.new()

        "Init 3 LandingZones"
        self.zone1 = Landing(screen)
        self.zone2 = Landing(screen)
        self.zone3 = Landing(screen)

        "Randomly select 6 obstacles"
        self.Obstacles = (Rock1, Rock2, Rock3, Satellite1, Satellite2, Building3, Building1, Building2)
        choice1, choice2, choice3, choice4, choice5 = random.choice(self.Obstacles), random.choice(self.Obstacles), \
                                                      random.choice(self.Obstacles), random.choice(self.Obstacles), \
                                                      random.choice(self.Obstacles)
        self.c1, self.c2, self.c3, self.c4, self.c5 = choice1(), choice2(), choice3(), choice4(), choice5()

        self.Meteor1 = Meteors()
        self.Meteor1.randomMetors()
        self.Meteor2 = Meteors()
        self.Meteor2.randomMetors()
        self.Meteor3 = Meteors()
        self.Meteor3.randomMetors()
        self.Meteor4 = Meteors()
        self.Meteor4.randomMetors()
        self.Meteor5 = Meteors()
        self.Meteor5.randomMetors()


    "Displays the Landing Zones"
    def displayZones(self):
        self.zone1.show((55, 705))
        self.zone2.show((455, 705))
        self.zone3.show((955, 705))

    "Checks whether Landed"
    def checkLanded(self):
       if self.zone1.rect.colliderect(self.lander.rect) or self.zone2.rect.colliderect(self.lander.rect) or self.zone3.rect.colliderect(self.lander.rect):
            if self.lander.y_vel <= 5.0:
                return True

    "Displays Obstacles"
    def displayObstacles(self, screen):
        self.c1.show((1010, 335), screen)
        self.c2.show((456, 123), screen)
        self.c3.show((900, 100), screen)
        self.c4.show((700, 455), screen)
        self.c5.show((220, 366), screen)

    "Checks if lander has collided with Obstacles"
    def obstacleCollissionDetect(self):
        if self.lander.rect.colliderect(self.c1.rect) or self.lander.rect.colliderect(self.c2.rect) or self.lander.rect.colliderect(self.c3.rect) or self.lander.rect.colliderect(self.c4.rect) or self.lander.rect.colliderect(self.c5.rect):
            return True

    "Checks if meteor has collided with lander"
    def meteorCollissionDetect(self):
        if self.lander.rect.colliderect(self.Meteor1.rect) or self.lander.rect.colliderect(self.Meteor2.rect) or self.lander.rect.colliderect(self.Meteor3.rect) or self.lander.rect.colliderect(self.Meteor4.rect) or self.lander.rect.colliderect(self.Meteor5.rect):
            return True

    "Displays Meteors"
    def displayMeteors(self, screen):
        self.Meteor1.blitme(screen)
        self.Meteor1.keepItMove()

        self.Meteor2.blitme(screen)
        self.Meteor2.keepItMove()

        self.Meteor3.blitme(screen)
        self.Meteor3.keepItMove()

        self.Meteor4.blitme(screen)
        self.Meteor4.keepItMove()

        self.Meteor5.blitme(screen)
        self.Meteor5.keepItMove()

    "to execute when game over"
    # when game is over
    def gameOver(self, screen):
        self.printOnScreen(screen, "The GAME is OVER.", (400, 300), 60)

    "On screen text-writing"
    # on screen displays
    def printOnScreen(self, screen, text, xy, size=20):
        font = pygame.font.SysFont('Comic Sans MS', size)
        textSurface = font.render(text, True, (255, 255, 255))
        screen.blit(textSurface, xy)
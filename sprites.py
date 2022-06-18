import pygame, random, math


class Sprites(pygame.sprite.Sprite):
    def __init__(self, image, xy = (0, 0)):
        super(Sprites, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = xy


class Background(Sprites):
    def __init__(self):
        super(Background, self).__init__("resources/mars_background_instr.png", (0, 0))


class Thrust(Sprites):
    def __init__(self, xy):
        super(Thrust, self).__init__("resources/thrust.png", xy)


class Lander(Sprites):
    def __init__(self, screen):
        self.fuel = 500
        self.damage = 0
        self.altitude = 1000 * 0.665
        self.current_altitude = 0
        self.angle = 0

        self.x_vel = random.uniform(-1, 1)
        self.y_vel = random.uniform(0, 1)

        self.screen = screen
        super(Lander, self).__init__("resources/lander.png", (700, 665-self.altitude))

    def new(self):
        self.screen.blit(self.image, self.rect)

    def gravitate(self):
        if self.rect.left <= 0:
            self.rect.left = 1199
        elif self.rect.left >= 1200:
            self.rect.left = 1

        if self.altitude >= self.current_altitude:
            self.rect.top += self.y_vel
            self.rect.left += self.x_vel
        else:
            self.rect.top = 0

        self.y_vel += 0.07
        self.screen.blit(self.image, self.rect)
        self.current_altitude = self.altitude - self.rect.top

    def thrust(self):
        if self.altitude >= self.current_altitude and self.fuel > 0:
            self.rect.top += self.y_vel
            self.rect.left += self.x_vel
            self.fuel -= 50

            self.x_vel += 2.1 * math.sin(math.radians(-self.angle))
            self.y_vel -= 2.1 * math.cos(math.radians(self.angle))

            thrust = Thrust((self.rect.left+30, self.rect.top+60))
            self.screen.blit(thrust.image, thrust.rect)

        self.current_altitude = self.altitude - self.rect.top
        self.screen.blit(self.image, self.rect)

    def left(self):
        self.angle = 0
        self.angle += 15
        self.gravitate()

    def right(self):
        self.angle = 0
        self.angle -= 15
        self.gravitate()


class Landing(Sprites):
    def __init__(self, screen):
        self.screen = screen

        super(Landing, self).__init__("resources/landingPads/pad.png")


    def show(self, xy):
        self.rect.left, self.rect.top = xy
        self.screen.blit(self.image, self.rect)

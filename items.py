import pygame, random


class Items(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Items, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen = None

    def show(self, xy, screen):
        self.screen = screen
        self.rect.left, self.rect.top = xy
        self.screen.blit(self.image, self.rect)


class Rock1(Items):
    def __init__(self):
        super(Rock1, self).__init__("resources/obstacles/rocks_NW.png")


class Rock2(Items):
    def __init__(self):
        super(Rock2, self).__init__("resources/obstacles/rocks_ore_SW.png")


class Rock3(Items):
    def __init__(self):
        super(Rock3, self).__init__("resources/obstacles/rocks_small_SE.png")


class Satellite1(Items):
    def __init__(self):
        super(Satellite1, self).__init__("resources/obstacles/satellite_SE.png")


class Satellite2(Items):
    def __init__(self):
        super(Satellite2, self).__init__("resources/obstacles/satellite_SW.png")


class Building1(Items):
    def __init__(self):
        super(Building1, self).__init__("resources/obstacles/building_station_NE.png")


class Building2(Items):
    def __init__(self):
        super(Building2, self).__init__("resources/obstacles/building_station_SW.png")


class Building3(Items):
    def __init__(self):
        super(Building3, self).__init__("resources/obstacles/building_dome.png")



class Meteors(Items):
    def __init__(self):
        super(Meteors, self).__init__("resources/meteors/spaceMeteors_003.png")

    def randomMetors(self):
        self.rect.left = random.uniform(400, 1000)
        self.rect.top = random.uniform(-60, -200)

    def keepItMove(self):
        if self.rect.left <= 0 or self.rect.top >= 700:
            self.randomMetors()

        self.rect.top += 7
        self.rect.left -= random.uniform(-1, 6)

    def blitme(self, screen):
        screen.blit(self.image, self.rect)

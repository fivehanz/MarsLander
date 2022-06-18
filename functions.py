import pygame, sys, random

def check(Player):
    for e in pygame.event.get():
        if e.type is pygame.QUIT:
            sys.exit()
        elif e.type is pygame.KEYDOWN and Player.lander.damage < 1000:
            if e.key == pygame.K_RIGHT:
                Player.lander.right()
            elif e.key == pygame.K_LEFT:
                Player.lander.left()
            elif e.key == pygame.K_SPACE:
                Player.lander.thrust()


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


def random_control_failures():
    if random.uniform(0, 1) > 0.98:
        if random.uniform(0, 1) < 0.3:
            return True

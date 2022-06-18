import pygame, sys, time
from sprites import Background
from player import Player
import functions as fun


pygame.init()

gameDisplay = pygame.display.set_mode((1200, 750))

pygame.display.set_caption("Mars Lander")

Clock = pygame.time.Clock()
exitGame = False
Background = Background()
Player = Player()

while not exitGame:
    if Player.lives == 0:
        Player.gameOver(gameDisplay)
        pygame.display.update()
        time.sleep(5)
        exitGame = True
    else:
        Player.begin(gameDisplay)

    # Run Loop unitl gameOver
    while Player.lives > 0:
        Clock.tick(15)
        # Init background Image
        gameDisplay.blit(Background.image, Background.rect)

        # Checks keypress events and exit/quit
        fun.check(Player)


        Player.lander.gravitate()
        Player.displayZones()
        if Player.checkLanded() is True:
            Player.score += 50
            Player.printOnScreen(gameDisplay, "PAUSED UNTIL KEYDOWN", (155, 88))
            pygame.display.flip()
            fun.wait()
            break
        elif Player.lander.current_altitude <= -2 or Player.lander.damage == 1000:
            Player.lives -= 1
            Player.printOnScreen(gameDisplay, "PAUSED UNTIL KEYDOWN", (155, 88))
            Player.lander.damage = 1000
            Player.printOnScreen(gameDisplay, str(int(round(Player.lander.damage/10))), (95, 62))
            Player.printOnScreen(gameDisplay, "YOU HAVE CRASHED!", (420, 200), 40)
            pygame.display.flip()
            fun.wait()
            break



        Player.displayObstacles(gameDisplay)
        if Player.obstacleCollissionDetect() is True:
            Player.lander.damage += 10

        Player.displayMeteors(gameDisplay)
        if Player.meteorCollissionDetect() is True:
            Player.lander.damage += 25


        Player.printOnScreen(gameDisplay, str(int(round((Player.lander.current_altitude/665) * 1000))), (260, 15))
        Player.printOnScreen(gameDisplay, str(round(Player.lander.y_vel, 3)), (280, 60))
        Player.printOnScreen(gameDisplay, str(round(Player.lander.x_vel, 3)), (280, 40))
        Player.printOnScreen(gameDisplay, str(Player.lander.fuel), (70, 40))
        Player.printOnScreen(gameDisplay, str(int(round(Player.lander.damage/10))), (95, 62))
        Player.printOnScreen(gameDisplay, str(Player.score), (80, 88))

        if fun.random_control_failures() is True:
            Player.printOnScreen(gameDisplay, "ALERT", (155, 88))
            pygame.display.flip()
            time.sleep(2)

        pygame.display.update()

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *



def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(000000)
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60))/1000 #framerate limit: 60fps


if __name__ == "__main__":
    main()
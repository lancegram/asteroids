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
    dt =0 
    flag_updated_move = False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.rotate(-dt)
                if event.key == pygame.K_d:
                    player.rotate(dt)
                flag_updated_move = True
            

        screen.fill(000000)
        if not flag_updated_move == True: player.update(dt)
        else: flag_updated_move = False
        player.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60))/1000 #framerate limit: 60fps


if __name__ == "__main__":
    main()
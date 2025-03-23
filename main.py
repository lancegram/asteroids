# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    clock = pygame.time.Clock()
    dt =0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)#putting Player objects in containers
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) 

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots,updatable,drawable)

    while True : #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return      #exits the game
            
            #elif event.type == pygame.KEYDOWN: #for catching soft taps
            #    if event.key == pygame.K_a:     #
            #        player.rotate(-dt)          #         
            #    if event.key == pygame.K_d:     #    
            #        player.rotate(dt)           #
            #    if event.key == pygame.K_w:     #
            #        player.move(dt)             #
            #    if event.key == pygame.K_s:     #
            #        player.move(-dt)            #
            #    flag_updated_move = True #need to initialise first
            #this part is deprecated and remains as an idea suggestion

        screen.fill(000000)

        updatable.update(dt)
        
        for sprite in asteroids:
            if sprite.is_colliding(player):
                print("Game over!")
                return      #exits the game

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60))/1000 #framerate limit: 60fps


if __name__ == "__main__":
    main()
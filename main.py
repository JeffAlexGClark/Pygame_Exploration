#Import pygame to allow us to use the open source library
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asterioids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (updatable, drawable, asterioids)

    AsteroidField.containers = (updatable)

    Shot.containers = (updatable, drawable, shots_group)


    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteriod_field = AsteroidField()

    game_on = 1
    
    while game_on > 0:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for objects in drawable:
            objects.draw(screen)

        updatable.update(dt)

        pygame.display.flip()

        for asteroid in asterioids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asterioids:
            for bullet in shots_group:
                if bullet.collide(asteroid):
                    asteroid.split()
                    bullet.kill()

        
        game_clock.tick(60)
        
        dt = game_clock.tick(60)/1000

    





if __name__ == "__main__":
    main()

import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=(SCREEN_WIDTH/2), y=(SCREEN_HEIGHT/2))
    astroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.collision_check(player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision_check(item) == True:
                    item.split()
        

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        last_tick_time = game_clock.tick(60)
        dt = last_tick_time / 1000

        

if __name__ == "__main__":
    main()


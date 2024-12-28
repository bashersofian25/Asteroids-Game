# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random

def split_or_kill(asteroid, field):
    random_angle = random.uniform(20, 50)
    new_radius = asteroid.radius/2
    if(new_radius < ASTEROID_MIN_RADIUS):
        asteroid.kill()
    else:
        first_velocity = 1.2*asteroid.velocity.rotate(-1*random_angle)
        second_velocity = 1.2*asteroid.velocity.rotate(random_angle)
        field.spawn(new_radius, asteroid.position, first_velocity)
        field.spawn(new_radius, asteroid.position, second_velocity)
        asteroid.kill()
        
    

def main():
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (drawable,updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.checkCollisions(asteroid):
                    shot.kill()

                    split_or_kill(asteroid=asteroid, field=field)

                            

        for object in drawable:
            object.draw(screen)
        
        for object in updatable:
            object.update(dt)
            if type(object) == Player:
                object.shoot()
            if type(object) == Asteroid and player1.checkCollisions(object):
                print('Game over!')
                exit()
        
        dt = clock.tick()/1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
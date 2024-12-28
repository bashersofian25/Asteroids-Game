import pygame
from circleshape import CircleShape
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.move(dt)


    def move(self, dt):
        self.position +=  self.velocity * dt * PLAYER_SHOOT_SPEED
        
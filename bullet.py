import pygame


class Bullet:

    def __init__(self, surface, position, speed, dx, dy):
        self.surface = surface
        self.position = position
        self.speed = speed
        self.dx = dx
        self.dy = dy

    def draw(self):
        pygame.draw.circle(self.surface, (255, 0, 0), self.position, 1)
        

    def collidewith(self):
        pass

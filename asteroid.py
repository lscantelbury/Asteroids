import pygame
import random
from constants import *
from pygame.constants import *





class Asteroid:
    def __init__(self, surface, position, sprite, size, dx, dy, speed, collision):
        self.surface = surface
        self.position = list(position)
        self.sprite = sprite
        self.size = self.sprite.get_size()
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.collision = collision

    def draw_asteroid(self):

        if self.size == LARGE_ASTEROID:
            self.sprite = pygame.transform.scale(self.sprite, LARGE_ASTEROID)
        if self.size == NORMAL_ASTEROID:
            self.sprite = pygame.transform.scale(self.sprite, NORMAL_ASTEROID)
        if self.size == LITTLE_ASTEROID:
            self.sprite = pygame.transform.scale(self.sprite, LITTLE_ASTEROID)
            
        self.surface.blit(self.sprite, self.position)

    def move_asteroid(self):
        if self.dx == 'RIGHT':
            self.position[0] += self.speed
        if self.dx == 'LEFT':
            self.position[0] -= self.speed

        if self.dy == 'UP':
            self.position[1] -= self.speed
        if self.dy == 'DOWN':
            self.position[1] += self.speed

        # Asteroid crossing movements through screen
        if self.position[0] > 800:  # Crossing horizontally
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = 800

        if self.position[1] > 600:  # Crossing vertically
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = 600

    def split_asteroid(self):
                 
        if self.size == LARGE_ASTEROID:
            self.sprite = pygame.transform.scale(self.sprite, NORMAL_ASTEROID)
            self.size = NORMAL_ASTEROID
            self.speed += 0.25
            self.collision = False
        elif self.size == NORMAL_ASTEROID:
            self.sprite = pygame.transform.scale(self.sprite, LITTLE_ASTEROID)
            self.size = LITTLE_ASTEROID
            self.speed += 0.25
            self.collision = False
        elif self.size == LITTLE_ASTEROID:
            return None

        dxs, dys = ['LEFT', 'RIGHT'], ['UP', 'DOWN']
        random.shuffle(dxs)
        random.shuffle(dys)


        return [Asteroid(self.surface, self.position, self.sprite, self.size,
                dxs[0], dys[0], self.speed, self.collision),
                Asteroid(self.surface, self.position, self.sprite, self.size,
                dxs[1], dys[1], self.speed, self.collision)] 

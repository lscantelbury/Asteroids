import pygame
import random
from constants import *
from pygame.constants import *





class Asteroid:
    def __init__(self, surface, position, sprite, size, dx, dy, speed):
        self.surface = surface
        self.position = list(position)
        self.sprite = sprite
        self.size = self.sprite.get_size()
        self.dx = dx
        self.dy = dy
        self.speed = speed

    def draw_asteroid(self):
        self.surface.blit(self.sprite, self.position)
        # pygame.draw.circle(self.surface, self.color, self.position, self.size)

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

        self.collision = False
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_s:
                    self.collision = True
        if self.collision == True:           
            if self.size == LARGE_ASTEROID:
                self.sprite = pygame.transform.scale(self.sprite, NORMAL_ASTEROID)
                self.size = NORMAL_ASTEROID
                self.collision = False
            elif self.size == NORMAL_ASTEROID:
                self.sprite = pygame.transform.scale(self.sprite, LITTLE_ASTEROID)
                self.size = LITTLE_ASTEROID
                self.collision = False
            elif self.size == LITTLE_ASTEROID:
                return None

        dxs, dys = ['LEFT', 'RIGHT'], ['UP', 'DOWN']
        random.shuffle(dxs)
        random.shuffle(dys)


        return [Asteroid(self.surface, self.position, self.sprite, self.size,
                dxs[0], dys[0], self.speed),
                Asteroid(self.surface, self.position, self.sprite, self.size,
                dxs[1], dys[1], self.speed)]


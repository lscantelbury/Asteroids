import random
import pygame
from pygame.image import load

from constants import *
from asteroid import Asteroid
from player import Spaceship
from pygame.constants import *
# from ufo import UFO


class Screen:
    def __init__(self):
        self._init_pygame()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = load(f"assets/sprites/space.png")
        self.clock = pygame.time.Clock()
        self.asteroid_sprite = load(f"assets/sprites/asteroid.png")
        self.asteroids = [
            Asteroid(self.screen, random.choice(position), self.asteroid_sprite, random.choice(sizes),
                     random.choice(init_dx), random.choice(init_dy), 0.25, False),
            Asteroid(self.screen, random.choice(position), self.asteroid_sprite, random.choice(sizes),
                     random.choice(init_dx), random.choice(init_dy), 0.25, False),
            Asteroid(self.screen, random.choice(position), self.asteroid_sprite, random.choice(sizes),
                     random.choice(init_dx), random.choice(init_dy), 0.25, False),
            Asteroid(self.screen, random.choice(position), self.asteroid_sprite, random.choice(sizes),
                     random.choice(init_dx), random.choice(init_dy), 0.25, False)
        ]
        'self.ufo = UFO()'
        self.spaceship = Spaceship((400, 300))

    def main_loop(self):
        while True:
            self._handle_input()
            self.draw_hud()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()

        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()
        if is_key_pressed[pygame.K_DOWN]:
            self.spaceship.slow_down()
            
    def _process_game_logic(self):
        self.spaceship.move(self.screen)
            
    def draw_hud(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        self.spaceship.move(self.screen)

        for asteroid in self.asteroids:
            asteroid.draw_asteroid()
            asteroid.move_asteroid()
            screen.collision()
            if asteroid.collision == True:
                asteroid.split_asteroid()
                self.asteroids.append(asteroid.split_asteroid)
        

        pygame.display.flip()
        self.clock.tick(60)

    def draw_elements(self):
        pass


if __name__ == "__main__":
    screen = Screen()
    screen.main_loop()

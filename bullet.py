import pygame


class Bullet:

    def __init__(self, surface, position):
        self.surface = surface
        self.position = position

    def draw(self):
        pygame.draw.circle(self.surface, (255, 255, 255), self.position, 5)

    def move(self):
        print(self.position)

        self.position = [self.position[0] + 5, self.position[1] + 5]

        if self.position[0] > 800 or self.position[0] < 0:  # Crossing horizontally
            return None
        if self.position[1] > 600 or self.position[1] < 0:  # Crossing vertically
            return None


    def collidewith(self):
        pass

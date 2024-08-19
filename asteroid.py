import pygame
import random
import math

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, size, x_screen, y_screen):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image_original = pygame.image.load(f'{self.size}.png')
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x_screen = x_screen
        self.y_screen = y_screen
        self.angle = random.randint(0, 360)
        self.speed = random.randint(1, 3)
        self.direction = random.uniform(0, 2 * math.pi)
        
    def update(self):
        # Move the asteroid
        self.rect.x += int(self.speed * math.cos(self.direction))
        self.rect.y += int(self.speed * math.sin(self.direction))

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = self.x_screen
        if self.rect.left > self.x_screen:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = self.y_screen
        if self.rect.top > self.y_screen:
            self.rect.bottom = 0

    def split(self):
        # Split the asteroid into two smaller ones if its size is greater than 1
        if self.size > 1:
            new_size = self.size - 1
            return [Asteroid(self.rect.centerx, self.rect.centery, new_size, self.x_screen, self.y_screen) for _ in range(2)]
        else:
            return []

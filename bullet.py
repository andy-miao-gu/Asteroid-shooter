import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle,x_screen, y_screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        # Rotate the bullet image so it's facing the right direction
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 50
        self.x_screen = x_screen
        self.y_screen = y_screen

    def update(self):
        rad_angle = math.radians(-self.angle)
        self.rect.x += int(self.speed * math.cos(rad_angle))
        self.rect.y += int(self.speed * math.sin(rad_angle))

        # Remove the bullet if it moves off the screen
        if (self.rect.x < 0 or self.rect.x > self.x_screen or
            self.rect.y < 0 or self.rect.y > self.y_screen):
            self.kill()



import pygame
import math

class Shooter(pygame.sprite.Sprite):
    '''This class will draw image 1 on slow speed and image 2 on high speed, and will rotate based on movement direction.'''

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = pygame.image.load('High speed_cropped.png')
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = 0
        self.speed = 5
        self.high_speed = False
        self.moving_forward = False
        self.turning_left = False
        self.turning_right = False
        self.imag_category = 1

    def update(self):
        if self.imag_category == 1:
            self.image_original = pygame.image.load('Stop moving or slow speed_croped.png')
        elif self.imag_category == 2:
            self.image_original = pygame.image.load('High speed_cropped.png')
        elif self.imag_category == 3:
            self.image_original = pygame.image.load('Drill.png')
        
        # Rotate the image based on the current angle
        self.image = pygame.transform.rotate(self.image_original, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Handle movement
        if self.turning_left:
            self.angle += 5
        if self.turning_right:
            self.angle -= 5

        if self.moving_forward:
            constant = 3 if self.high_speed else 1
            rad_angle = math.radians(-self.angle)
            self.rect.x += int(constant*self.speed * math.cos(rad_angle))
            self.rect.y += int(constant*self.speed * math.sin(rad_angle))

    def move_forward(self):
        self.moving_forward = True

    def stop_moving(self):
        self.moving_forward = False

    def turn_left(self):
        self.turning_left = True

    def stop_turning_left(self):
        self.turning_left = False

    def turn_right(self):
        self.turning_right = True

    def stop_turning_right(self):
        self.turning_right = False

    

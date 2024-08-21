# move a rock randomly in space path is rocks_folder/1.png 

import pygame
import random
import os

class myRock(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(os.path.join("rocks_folder", "1.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, self.screen.get_width())
        self.rect.centery = random.randint(0, self.screen.get_height())
        self.speed = random.randint(1, 3)
        self.angle = random.randint(0, 360)
        self.angle_speed = random.randint(0, 10)

    def update(self):
        self.rect.centerx += self.speed * (self.angle % 360)
        self.rect.centery += self.speed * (self.angle % 360)
        self.angle += self.angle_speed
        if self.rect.left > self.screen.get_width():
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = self.screen.get_width()
        if self.rect.top > self.screen.get_height():
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = self.screen.get_height()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image

    def get_speed(self):
        return self.speed

    def get_angle(self):
        return self.angle

    def get_angle_speed(self):
        return self.angle_speed

    def set_speed(self, speed):
        self.speed = speed

    def set_angle(self, angle):
        self.angle = angle

    def set_angle_speed(self, angle_speed):
        self.angle_speed = angle_speed

    def set_position(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def set_image(self, image):
        self.image = image

    def set_rect(self, rect):
        self.rect = rect

    def set_angle(self, angle):
        self.angle = angle

    def set_angle_speed(self, angle_speed):
        self.angle_speed = angle_speed

    def set_speed(self, speed):
        self.speed = speed

    def set_position(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def set_image(self, image):
        self.image = image


if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rocks")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    rock = myRock(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rock.update()
        rock.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
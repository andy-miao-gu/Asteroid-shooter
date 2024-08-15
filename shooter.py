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

    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        # Rotate the bullet image so it's facing the right direction
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 50

    def update(self):
        rad_angle = math.radians(-self.angle)
        self.rect.x += int(self.speed * math.cos(rad_angle))
        self.rect.y += int(self.speed * math.sin(rad_angle))

        # Remove the bullet if it moves off the screen
        if (self.rect.x < 0 or self.rect.x > 800 or
            self.rect.y < 0 or self.rect.y > 600):
            self.kill()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Shooter')

    clock = pygame.time.Clock()

    shooter = Shooter(400, 300)
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(shooter)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shooter.turn_left()
                if event.key == pygame.K_RIGHT:
                    shooter.turn_right()
                if event.key == pygame.K_UP:
                    shooter.move_forward()
                if event.key == pygame.K_SPACE:
                    shooter.high_speed = True 
                    shooter.imag_category = 2
                if event.key == pygame.K_d:
                    shooter.imag_category = 3
                if event.key == pygame.K_f:
                    # Fire a bullet
                    bullet = Bullet(shooter.rect.centerx, shooter.rect.centery, shooter.angle)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    shooter.stop_turning_left()
                if event.key == pygame.K_RIGHT:
                    shooter.stop_turning_right()
                if event.key == pygame.K_UP:
                    shooter.stop_moving()
                if event.key == pygame.K_SPACE:
                    shooter.high_speed = False
                    shooter.imag_category = 1
                if event.key == pygame.K_d:
                    shooter.imag_category = 1
                
        # Update all sprites
        all_sprites.update()

        # Draw everything
        screen.fill((0, 0, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

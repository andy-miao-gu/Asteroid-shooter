import pygame
import math
from shooter import Shooter
from bullet import Bullet


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

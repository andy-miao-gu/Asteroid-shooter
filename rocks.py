import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Break")

# Load images
rock_image = pygame.image.load("1.png")
object_image = pygame.image.load("3.png")

# Rock class
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = rock_image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.broken = False

    def update(self):
        if self.broken:
            for obj in objects:
                obj.update()
        else:
            self.rect.x += random.uniform(-1, 1)  # Simulate random movement
            self.rect.y += random.uniform(-1, 1)  # Simulate random movement

            # Keep the rock within screen bounds
            self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
            self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def break_rock(self):
        self.broken = True
        for _ in range(3):
            obj = SpaceObject()
            objects.add(obj)
            all_sprites.add(obj)

# SpaceObject class
class SpaceObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = object_image
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Keep the object within screen bounds
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity.x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity.y *= -1

# Setup
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()
rock = Rock()
all_sprites.add(rock)

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not rock.broken:
                rock.break_rock()

    all_sprites.update()

    screen.fill((0, 0, 0))  # Clear screen with black
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

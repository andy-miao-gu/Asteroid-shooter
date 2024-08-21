import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Breaking Rock')

# Load rock images
rock_image_large = pygame.image.load('rocks_folder/1.png')  # Large rock
rock_image_small = pygame.image.load('rocks_folder/2.png')  # Small rocks after breaking

class myRock(pygame.sprite.Sprite):
    def __init__(self, image, x, y, is_large=True):
        super().__init__()
        self.is_large = is_large
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

        # If the rock is large, give it slow speed; smaller rocks move faster
        self.speed_x = random.randint(-3, 3) if self.is_large else random.randint(-5, 5)
        self.speed_y = random.randint(-3, 3) if self.is_large else random.randint(-5, 5)

    def update(self):
        # Move the rock
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # If the rock goes out of bounds, reset it
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        # Regenerate a new rock at a random position within bounds
        if self.is_large:
            self.image = rock_image_large
        else:
            self.image = rock_image_small
        self.rect = self.image.get_rect(
            center=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        )
        self.speed_x = random.randint(-3, 3) if self.is_large else random.randint(-5, 5)
        self.speed_y = random.randint(-3, 3) if self.is_large else random.randint(-5, 5)

    def break_rock(self):
        # Break the large rock into two smaller rocks
        if self.is_large:
            rock1 = myRock(rock_image_small, self.rect.centerx, self.rect.centery, is_large=False)
            rock2 = myRock(rock_image_small, self.rect.centerx, self.rect.centery, is_large=False)
            return [rock1, rock2]
        return []

def main():
    clock = pygame.time.Clock()

    # Sprite group to manage all rocks
    all_rocks = pygame.sprite.Group()

    # Create the initial large rock and add it to the group
    initial_rock = myRock(rock_image_large, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    all_rocks.add(initial_rock)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Break the rock when space is pressed
                for rock in all_rocks:
                    if rock.is_large:  # Only break large rocks
                        new_rocks = rock.break_rock()
                        all_rocks.add(new_rocks)
                        rock.kill()  # Remove the original large rock

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update and draw all rocks
        all_rocks.update()
        all_rocks.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

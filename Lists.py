import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
SKY_BLUE = (135, 206, 235)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rage Climb")

# Define player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.spawn_at_random_platform()  # Call spawn method in constructor
        self.vel_x = 0
        self.vel_y = 0
        self.score = 0
        self.is_jumping = False
        self.jump_cooldown = 0
        self.remaining_jumps = 3  # Number of available jumps

    def spawn_at_random_platform(self):
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.rect.bottom = 0  # Spawn on top of the screen initially

    def update(self):
        self.apply_friction()

        # Apply gravity
        self.vel_y += 0.5

        # Check bottom and side boundaries
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT  # Ensure player stays within screen bounds
            self.vel_y = 0

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Handle collision with platforms
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if self.vel_y > 0:  # Player falling, colliding with platform top
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.is_jumping = False
                self.remaining_jumps = 3  # Reset remaining jumps when landing

    def apply_friction(self):
        if self.vel_x > 0:
            self.vel_x -= 0.2  # Apply friction to the right
            if self.vel_x < 0:
                self.vel_x = 0  # Ensure velocity doesn't go negative
        elif self.vel_x < 0:
            self.vel_x += 0.2  # Apply friction to the left
            if self.vel_x > 0:
                self.vel_x = 0  # Ensure velocity doesn't go positive



    def jump(self):
        if self.remaining_jumps > 0:
            self.vel_y = -10
            self.is_jumping = True
            self.remaining_jumps -= 1

# Define platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create player and platform objects
player = Player()
platforms = pygame.sprite.Group()

# Add bottom platform
bottom_platform = Platform(0, HEIGHT - 20, WIDTH, 20)
platforms.add(bottom_platform)

# Font for meter display
font = pygame.font.Font(None, 36)

# Spawn percentage for platforms
spawn_percentage = 0.3

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.vel_x = -5
    elif keys[pygame.K_d]:
        player.vel_x = 5
    else:
        player.vel_x = 0

    # Update game objects
    player.update()

    # Spawn platforms from bottom to top
    while len(platforms) < 20:
        platform_x = random.randint(0, WIDTH - 50)
        platform_y = random.randint(HEIGHT - 20, HEIGHT + 100)  # Generate platforms below and slightly above the screen
        if random.random() < spawn_percentage:  # Adjust spawn probability
            platform = Platform(platform_x, platform_y, 50, 10)
            platforms.add(platform)
        else:
            break  # Exit loop if the platform reaches maximum platforms or does not meet spawn probability

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define screen size
WIDTH = 800
HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Start in the center
        self.dx = 0  # Change in x position (movement)
        self.dy = 0  # Change in y position (movement)
        self.speed = 5  # Movement speed
        self.body = [self.rect]  # List to store snake body segments

    def update(self):
        # Update head position based on movement
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for wall collisions
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.die()

        # Check for collision with own body
        for segment in self.body[:-1]:  # Exclude head
            if self.rect.colliderect(segment):
                self.die()

        # Add new head segment and remove tail if grown from eating food
        self.body.append(self.body[-1].copy())  # Copy the last segment
        self.body[-1].center = (self.rect.centerx + self.dx, self.rect.centery + self.dy)
        if len(self.body) > 1 and self.grow:  # If grown from eating food, remove tail
            self.body.pop(0)
            self.grow = False  # Reset grow flag

    def die(self):
        print("Game Over!")
        self.body = [self.rect]  # Reset snake to starting state
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = 0
        self.dy = 0

    def change_direction(self, x, y):
        # Only change direction if not moving in the opposite direction
        if x != -self.dx and y != -self.dy:
            self.dx = x
            self.dy = y

    def grow(self):
        self.grow = True  # Flag to indicate snake should grow after update

# Define food class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

    def spawn(self):
        # Randomly place food within screen boundaries
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

# Create snake and food objects
snake = Snake()
food = Food()

# Game loop variables
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # For score display
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change snake direction based on key press
            if event.key == pygame.K_LEFT:
                snake.change_direction(-snake.speed, 0)
            elif event.key == pygame.K_RIGHT:
                print("h")


    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

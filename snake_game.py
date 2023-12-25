import pygame
import sys
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10
SCORE_FONT_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Green color
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN  # Green color

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = WHITE
        self.radius = GRID_SIZE // 2  # Radius for round shape
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.position[0] + self.radius, self.position[1] + self.radius),
                           self.radius)

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()

    score = 0
    start_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake.direction = RIGHT

        snake.update()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()
            score += 1
            start_time = time.time()

        surface.fill(BLACK)
        snake.render(surface)
        food.render(surface)

        # Display the score
        font = pygame.font.Font(None, SCORE_FONT_SIZE)
        score_text = font.render(f"Score: {score}", True, WHITE)
        surface.blit(score_text, (10, 10))

        # Display the time spent per feed
        elapsed_time = time.time() - start_time
        time_text = font.render(f"Time: {int(elapsed_time)}s", True, WHITE)
        surface.blit(time_text, (10, 40))

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

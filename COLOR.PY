import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Catcher")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bucket
bucket_width = 100
bucket_height = 20
bucket = pygame.Rect(WIDTH // 2 - bucket_width // 2, HEIGHT - 40, bucket_width, bucket_height)
bucket_color = (200, 0, 225)
bucket_speed = 10

# Ball
ball_radius = 20
ball_speed = 5

def create_ball():
    x = random.randint(ball_radius, WIDTH - ball_radius)
    color = random.choice(BALL_COLORS)
    return {'x': x, 'y': 0, 'color': color}

balls = [create_ball()]
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill(WHITE)
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move bucket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bucket.left > 0:
        bucket.x -= bucket_speed
    if keys[pygame.K_RIGHT] and bucket.right < WIDTH:
        bucket.x += bucket_speed

    # Update and draw balls
    for ball in balls:
        ball['y'] += ball_speed
        pygame.draw.circle(screen, ball['color'], (ball['x'], ball['y']), ball_radius)

        # Collision with bucket
        if (bucket.collidepoint(ball['x'], ball['y'] + ball_radius)):
            score += 1
            balls.remove(ball)
            balls.append(create_ball())
        elif ball['y'] > HEIGHT:
            balls.remove(ball)
            balls.append(create_ball())

    # Draw bucket
    pygame.draw.rect(screen, bucket_color, bucket)

    # Display Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
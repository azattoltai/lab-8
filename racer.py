import pygame
import random

pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Түстер
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Ойын параметрлері
car_width, car_height = 60, 80
enemy_width, enemy_height = 60, 80
coin_size = 30
speed = 7
score = 0
running = True

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    render_text = font.render(text, True, color)
    text_rect = render_text.get_rect(center=(x, y))
    screen.blit(render_text, text_rect)

# Ойын объектілері
player_x = WIDTH // 2 - car_width // 2
player_y = HEIGHT - car_height - 20

enemies = []
coins = []

def create_enemy():
    x = random.randint(60, WIDTH - enemy_width - 60)
    y = -enemy_height
    enemies.append([x, y])

def create_coin():
    x = random.randint(60, WIDTH - coin_size - 60)
    y = -coin_size
    coins.append([x, y])

clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= 7
    if keys[pygame.K_RIGHT] and player_x < WIDTH - car_width - 50:
        player_x += 7
    
    if random.randint(1, 40) == 1:
        create_enemy()
    if random.randint(1, 60) == 1:
        create_coin()
    
    # Жаулар қозғалысы
    for enemy in enemies[:]:
        enemy[1] += speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))
        if (player_x < enemy[0] + enemy_width and player_x + car_width > enemy[0] and
            player_y < enemy[1] + enemy_height and player_y + car_height > enemy[1]):
            running = False
    
    # Монеталар қозғалысы
    for coin in coins[:]:
        coin[1] += speed
        if coin[1] > HEIGHT:
            coins.remove(coin)
        pygame.draw.circle(screen, YELLOW, (coin[0] + coin_size // 2, coin[1] + coin_size // 2), coin_size // 2)
        if (player_x < coin[0] + coin_size and player_x + car_width > coin[0] and
            player_y < coin[1] + coin_size and player_y + car_height > coin[1]):
            score += 1
            coins.remove(coin)
    
    pygame.draw.rect(screen, WHITE, (player_x, player_y, car_width, car_height))
    draw_text(f"Score: {score}", 30, WHITE, 70, 30)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

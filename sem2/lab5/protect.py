import mpl_toolkits.mplot3d.art3d
import pygame
import sys
import math

# Глобальные константы
WIDTH = 1200
HEIGHT = 800
FPS = 30
TANK_COLOR = (17, 82, 34)

# Инициализируем все необходимые для окна параметры
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x, y = 0, HEIGHT // 2
dx = 70
angle = 0
while True:
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, TANK_COLOR, [[x, y], [x + 40, y + 80], [x + 440, y + 80], [x + 480, y], [x + 400, y],
                                             [x + 370, y - 60], [x + 540, y - 60], [x + 540, y - 80], [x + 360, y - 80],
                                             [x + 350, y - 100], [x + 130, y - 100], [x + 80, y]])

    pygame.draw.circle(screen, (0, 0, 0), (x + 90, y + 110), 40)
    pygame.draw.circle(screen, (0, 0, 0), (x + 190, y + 110), 40)
    pygame.draw.circle(screen, (0, 0, 0), (x + 290, y + 110), 40)
    pygame.draw.circle(screen, (0, 0, 0), (x + 390, y + 110), 40)

    pygame.draw.circle(screen, (255, 255, 255), (x + dx, y + 90), 5)
    pygame.draw.circle(screen, (255, 255, 255), (x + dx + 100, y + 90), 5)
    pygame.draw.circle(screen, (255, 255, 255), (x + dx + 200, y + 90), 5)
    pygame.draw.circle(screen, (255, 255, 255), (x + dx + 300, y + 90), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    angle += 10
    dx = 10 * math.cos(math.radians(45 - 1 / 2 * angle)) + 70
    x += 2
    if x >= WIDTH:
        x = -540

    pygame.display.flip()
    clock.tick(FPS)



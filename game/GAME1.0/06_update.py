import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制飞机
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero, (200, 500))

# 统一更新
pygame.display.update()

while True:
    pass
pygame.quit()

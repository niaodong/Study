import pygame
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景
# 加载图像
bg = pygame.image.load("./images/background.png")
# blit绘制图像
screen.blit(bg, (0, 0))
# update更新图像
pygame.display.update()

# 绘制飞机
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

while True:
    pass
pygame.quit()

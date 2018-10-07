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

while True:
    pass
pygame.quit()
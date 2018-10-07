import pygame

# 游戏的初始化
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

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环
while True:
    # 指定代码执行频率
    clock.tick(60)

pygame.quit()

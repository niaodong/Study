import pygame
from plane_sprites import *

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

# 记录飞机初始位置
hero_rect = pygame.Rect(200, 500, 100, 124)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy0.png")
enemy1 = GameSprite("./images/enemy0.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环
while True:
    # 指定代码执行频率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # 判断是否为退出
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # quit卸载所有模块
            pygame.quit()
            # exit退出系统
            exit()

    # 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 精灵组调用两个方法 update-让组中所有精灵更新位置 drown-在screen绘制所有图像
    enemy_group.update()
    enemy_group.draw(screen)

    # update更新
    pygame.display.update()

pygame.quit()

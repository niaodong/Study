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

# 记录飞机初始位置
hero_rect = pygame.Rect(200, 500, 100, 124)
# 游戏循环
while True:
    # 指定代码执行频率
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    # 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机位置
    if hero_rect.y <= -124:
        hero_rect.y = 700
    # 绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # update更新
    pygame.display.update()

pygame.quit()
